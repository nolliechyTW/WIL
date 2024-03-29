public class DoubleHashingCRP implements CollisionResolutionPolicy {

    private int prime;
    private int M;

    public DoubleHashingCRP(int prime) {
        this.prime = prime;
    }

    @Override
    public int probe(Object key, int i) {
        int hashCode = key.hashCode();
        // Apply Math.abs here to avoid negative numbers due to integer overflow
        return Math.abs((hashCode + i * h2(key)) % M);
    }

    private int h2(Object key) {
        // Ensuring non-negative input for modulo operation
        return prime - (Math.abs(key.hashCode()) % prime);
    }


    @Override
    public void setUp(int tableSize) {
        M = tableSize;
    }

    @Override
    public String toString() {
        return String.format("Double Hashing using prime %d", prime);
    }
}
