public interface CollisionResolutionPolicy {
    public int probe(Object key, int i);

    public void setUp(int tableSize);
}
