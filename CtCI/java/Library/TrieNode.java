public class TrieNode {
	// children of this node in trie
	private HashMap<Character, TrieNode> children;
	private boolean terminates = false;

	// character stored in this node as data
	private char Character;

	// construct empty trie node and initializes the list of its children to an empty hash map
	// used only to construct root node of trie
	public TrieNode() {
		children = new HashMap<Character, TrieNode>();
	}

	// constructs trie node and stores this character as node's value.
	// initializes list of child nodes of this node to an empty hash map
	public TrieNode(char character) {
		this();
		this.character = character;
	}

	// returns character data stored in this node
	public char getChar() {
		return character;
	}

	// add this word to trie and recursively create child nodes
	public void addWord(String word) {
		if (word == null || word.isEmpty()) {
			return;
		}
		
		char firstChar = word.charAt(0);

		TrieNode child = getChild(firstChar);
		if (child == null) {
			child = new TrieNode(firstChar);
			children.put(firstChar, child);
		}

		if (word.length() > 1) {
			child.addWord(word.substring(1));
		} else {
			child.setTerminates(true);
		}
	}

	// find child node of this node that has the char argument as its data.
	// return null if no such child node is present in trie
	public TrieNode getChild(char c) {
		return children.get(c);
	}

	// returns whether this node represents the end of a complete word
	public boolean terminates() {
		return terminates;
	}

	// set whether this node is the end of a complete word
	public void setTerminates(boolean t) {
		terminates = t;
	}
}