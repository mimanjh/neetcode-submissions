class Node {
    private int key;
    private int value;
    private Node next;
    private Node prev;

    public Node(int key, int value) {
        this.key = key;
        this.value = value;
        this.next = null;
        this.prev = null;
    }

    public int getKey() {
        return this.key;
    }

    public void setKey(int key) {
        this.key = key;
    }

    public int getValue() {
        return this.value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public Node getNext() {
        return this.next;
    }
    public void setNext(Node next) {
        this.next = next;
    }

    public Node getPrev() {
        return this.prev;
    }
    public void setPrev(Node prev) {
        this.prev = prev;
    }
}
class LRUCache {
    // hashmap +  linkedlist combo with helper functions for linked list
    // remember that accessing data is also "using" the cache

    private int capacity;
    private Map<Integer, Node> cache;
    private Node left;
    private Node right;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        this.left = new Node(0, 0);
        this.right = new Node(0, 0);
        this.left.next = this.right;
        this.right.prev = this.left;
    }

    private void insert(Node b) {
        Node a = this.right.getPrev();
        Node c = this.right;

        b.next = c;
        b.prev = a;

        c.prev = b;
        a.next = b;
    }

    private void remove(Node b) {
        Node a = b.prev;
        Node c = b.next;

        a.next = c;
        c.prev = a;
    }
    
    public int get(int key) {
        // if key exists in cache, return key, otherwise return -1
        if (this.cache.containsKey(key)) {
            Node node = this.cache.get(key);
            this.remove(node);
            this.insert(node);
            return node.getValue();
        }
        return -1;
    }
    
    public void put(int key, int value) {
        // if key exists in cache, remove it
        // insert no matter what after updating
        if (this.cache.containsKey(key)) {
            this.remove(this.cache.get(key));
        }
        Node node = new Node(key, value);
        this.insert(node);
        this.cache.put(key, node);
        
        // if over capacity, remove the LRU key
        if (this.cache.size() > this.capacity) {
            Node LRU = this.left.getNext();
            this.remove(LRU);
            this.cache.remove(LRU.getKey());
        }
    }
}
