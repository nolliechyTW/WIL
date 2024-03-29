import java.util.Arrays;

public class OpenAddressingHashTable {

    private OpenAddressingBucket[] table;
    private CollisionResolutionPolicy crp;

    public OpenAddressingHashTable(int initialCapacity, CollisionResolutionPolicy crp) {
        table = new OpenAddressingBucket[initialCapacity];
        this.crp = crp;
        for (int i = 0; i < table.length; i++) {
            table[i] = OpenAddressingBucket.EMPTY_SINCE_START;
        }
    }

    // protected abstract int probe(Object key, int i);

    // Inserts the specified key/value pair. If the key already exists, the
    // corresponding value is updated. If inserted or updated, true is returned.
    // If not inserted, then false is returned.
    public int insert(Object key, Object value) {
        // First search for the key in the table. If found, update bucket's value.
        for (int i = 0; i < table.length; i++) {
            int bucketIndex = crp.probe(key, i);

            // An empty-since-start bucket implies the key is not in the table
            if (table[bucketIndex] == OpenAddressingBucket.EMPTY_SINCE_START) {
                break;
            }

            if (table[bucketIndex] != OpenAddressingBucket.EMPTY_AFTER_REMOVAL) {
                // Check if the non-empty bucket has the key
                if (key.equals(table[bucketIndex].key)) {
                    // Update the value
                    table[bucketIndex].value = value;
                    return i;
                }
            }
        }

        // The key is not in the table, so insert into first empty bucket
        for (int i = 0; i < table.length; i++) {
            int bucketIndex = crp.probe(key, i);
            if (table[bucketIndex].isEmpty()) {
                table[bucketIndex] = new OpenAddressingBucket(key, value);
                return i;
            }
        }

        return table.length - 1; // no empty bucket found
    }

    // Searches for the specified key. If found, the key/value pair is removed
    // from the hash table and true is returned. If not found, false is returned.
    public boolean remove(Object key) {
        for (int i = 0; i < table.length; i++) {
            int bucketIndex = crp.probe(key, i);

            // An empty-since-start bucket implies the key is not in the table
            if (table[bucketIndex] == OpenAddressingBucket.EMPTY_SINCE_START) {
                return false;
            }

            if (table[bucketIndex] != OpenAddressingBucket.EMPTY_AFTER_REMOVAL) {
                // Check if the non-empty bucket has the key
                if (key.equals(table[bucketIndex].key)) {
                    // Remove by setting the bucket to empty-after-removal
                    table[bucketIndex] = OpenAddressingBucket.EMPTY_AFTER_REMOVAL;
                    return true;
                }
            }
        }

        return false; // key not found
    }

    // Searches for the key, returning the corresponding value if found, null if
    // not found.
    public int search(Object key) {
        for (int i = 0; i < table.length; i++) {
            int bucketIndex = crp.probe(key, i);

            // An empty-since-start bucket implies the key is not in the table
            if (table[bucketIndex] == OpenAddressingBucket.EMPTY_SINCE_START) {
                return i;
            }

            if (table[bucketIndex] != OpenAddressingBucket.EMPTY_AFTER_REMOVAL) {
                // Check if the non-empty bucket has the key
                if (key.equals(table[bucketIndex].key)) {
                    return i;
                }
            }
        }

        return -1; // key not found
    }

    public OpenAddressingBucket[] getTableView() {
        return Arrays.copyOf(table, table.length);
    }

}
