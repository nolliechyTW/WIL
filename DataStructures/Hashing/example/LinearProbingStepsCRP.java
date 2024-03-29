public class LinearProbingStepsCRP implements CollisionResolutionPolicy {
    private int c;
    private int M;

    public LinearProbingStepsCRP(int i) {
        c = i;
    }

    @Override
    public int probe(Object key, int i) {
        return (Math.abs(key.hashCode()) + i * c) % M; // Ensures the result is always positive and within table bounds
    }

    @Override
    public void setUp(int tableSize) {
        M = tableSize;
    }

    @Override
    public String toString() {
        return String.format("Linear Probing with steps of %d", c);
    }
}
