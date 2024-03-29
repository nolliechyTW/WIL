public class LinearProbingCRP implements CollisionResolutionPolicy {

    private int M;
    @Override
    public int probe(Object key, int i) {
        return ((key.hashCode() + i) % M + M) % M; // Ensures the result is always positive
    }


    @Override
    public void setUp(int tableSize) {
        M = tableSize;
    }

    @Override
    public String toString() {
        return "Linear Probing";
    }
}
