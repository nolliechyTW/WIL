
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class HashingTest {
    @Test
    public void testQuadraticProbe() {
        int capacity = 10;
        CollisionResolutionPolicy crp = new QuadraticProbingCRP(5, 7);
        crp.setUp(capacity);
        OpenAddressingHashTable ht = new OpenAddressingHashTable(capacity, crp);
        int[] insertionKeys = { 880909, 612381939, 1102931209 };

        for (int i = 0; i < insertionKeys.length; i++) {
            ht.insert(insertionKeys[i], "dummy_" + i);
        }

        OpenAddressingBucket[] table = ht.getTableView();

        assertEquals(table[9].key, 880909);
        assertEquals(table[1].key, 612381939);
        assertEquals(table[7].key, 1102931209);
    }

    @Test
    public void testLinearProbe() {
        int capacity = 10;
        CollisionResolutionPolicy crp = new LinearProbingCRP();
        crp.setUp(capacity);
        OpenAddressingHashTable ht = new OpenAddressingHashTable(capacity, crp);
        int[] insertionKeys = { 880909, 612381939, 1102931209, 6019219, -523139 };

        for (int i = 0; i < insertionKeys.length; i++) {
            ht.insert(insertionKeys[i], "dummy_" + i);
        }

        OpenAddressingBucket[] table = ht.getTableView();

        assertEquals(table[9].key, 880909);
        assertEquals(table[0].key, 612381939);
        assertEquals(table[1].key, 1102931209);
        assertEquals(table[2].key, 6019219);
        assertEquals(table[3].key, -523139);
    }

    @Test
    public void testLinearProbeSteps() {
        int capacity = 10;
        CollisionResolutionPolicy crp = new LinearProbingStepsCRP(3);
        crp.setUp(capacity);
        OpenAddressingHashTable ht = new OpenAddressingHashTable(capacity, crp);
        int[] insertionKeys = { 880909, 612381939, 1102931209, 6019219, -523139 };

        for (int i = 0; i < insertionKeys.length; i++) {
            ht.insert(insertionKeys[i], "dummy_" + i);
        }

        OpenAddressingBucket[] table = ht.getTableView();

        assertEquals(table[9].key, 880909);
        assertEquals(table[2].key, 612381939);
        assertEquals(table[5].key, 1102931209);
        assertEquals(table[8].key, 6019219);
        assertEquals(table[1].key, -523139);
    }

    @Test
    public void testDoubleProbe() {
        int capacity = 10;
        CollisionResolutionPolicy crp = new DoubleHashingCRP(7);
        crp.setUp(capacity);
        OpenAddressingHashTable ht = new OpenAddressingHashTable(capacity, crp);
        int[] insertionKeys = { 880909, 612381939, 1102931209, 6019219, -523139 };

        for (int i = 0; i < insertionKeys.length; i++) {
            ht.insert(insertionKeys[i], "dummy_" + i);
        }

        OpenAddressingBucket[] table = ht.getTableView();

        assertEquals(table[9].key, 880909);
        assertEquals(table[5].key, 612381939);
        assertEquals(table[4].key, 1102931209);
        assertEquals(table[3].key, 6019219);
        assertEquals(table[7].key, -523139);
    }
}
