import java.util.Random;

/**
 * No TODOs in this file, just run it and see the results of the different
 * collision resolution policies.
 * Which one performs the best? What happens at different capacities and load
 * factors?
 */
public class Experiment {

    private static final long SEED = 5490L;

    private final double loadFactor;
    private final int capacity;
    private final Random r;

    public Experiment(double loadFactor, int capacity) {
        this.loadFactor = loadFactor;
        this.capacity = capacity;
        this.r = new Random(SEED);
    }

    public void runExperiment(CollisionResolutionPolicy crp) {
        crp.setUp(capacity);
        OpenAddressingHashTable ht = new OpenAddressingHashTable(capacity, crp);
        int[] insertProbeCountFrequencies = new int[capacity];
        int[] containsProbeCountFrequencies = new int[capacity];

        int numIterations = (int) (loadFactor * capacity);
        for (int i = 0; i < numIterations; i++) {
            insertProbeCountFrequencies[ht.insert(r.nextInt(), "dummy")]++;
        }
        for (int i = 0; i < numIterations; i++) {
            containsProbeCountFrequencies[ht.search(r.nextInt())]++;
        }

        double insertProbeCounts = 0;
        double containsProbeCounts = 0;
        for (int i = 0; i < insertProbeCountFrequencies.length; i++) {
            insertProbeCounts += insertProbeCountFrequencies[i] * (i + 1);
            containsProbeCounts += containsProbeCountFrequencies[i] * (i + 1);
        }
        insertProbeCounts /= numIterations;
        containsProbeCounts /= numIterations;

        System.out.printf("%s:%nAverage number of probes per element inserted: %4.2f%n", crp, insertProbeCounts);
        System.out.printf("Average number of probes per element searched after inserting %d keys: %4.2f%n",
                numIterations, containsProbeCounts);

        // reset the random seed so we can run the experiment again
        r.setSeed(SEED);

    }

    public static void main(String[] args) {
        double loadFactor = 0.75;
        int capacity = 10000;
        Experiment e = new Experiment(loadFactor, capacity);
        CollisionResolutionPolicy linearProbingCRP = new LinearProbingCRP();

        e.runExperiment(linearProbingCRP);
        e.runExperiment(new LinearProbingStepsCRP(17));
        e.runExperiment(new LinearProbingStepsCRP(2479));
        e.runExperiment(new QuadraticProbingCRP(7, 19));
        e.runExperiment(new DoubleHashingCRP(7));

    }
}
