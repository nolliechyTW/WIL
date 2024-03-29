public class QuadraticProbingCRP implements CollisionResolutionPolicy {

    private int c1;
    private int c2;
    private int M;

    public QuadraticProbingCRP(int c1, int c2) {
        this.c1 = c1;
        this.c2 = c2;
    }

    @Override
    public int probe(Object key, int i) {
        return (Math.abs(key.hashCode() % M) + c1 * i + c2 * i * i) % M;
    }

    @Override
    public void setUp(int tableSize) {
        this.M = tableSize;
    }

    @Override
    public String toString() {
        return String.format("Quadratic Probing with constants (%d, %d)", c1, c2);
    }
}
