package linked_lists;

class Node {
	Node next;
	int data;
	
	void appendToTail(int d) {
		Node end = new Node();
		end.data = d;
		Node n = this;
		while (n.next != null) {
			n = n.next;
		}
		n.next = end;
	}
	
	public static Node InsertNth (Node head, int data, int position) {
		
		//if head is null
		if (head == null) {
			head = new Node();
			head.data = data;
			return head;
		}
		

		Node prev, curr, newNode, next;
		newNode = new Node();
		newNode.data = data;
		
		//if position is 0
		if (position == 0) {
			newNode.next = head;
			head = newNode;
			return head;
		}
		
		curr = head;
		int counter = 1;
		while (curr.next != null && counter != position) {
			curr = curr.next;
			counter += 1;
		}
		//store next node;
		next = curr.next;
		//set cur.next t0 newNode
		curr.next = newNode;
		newNode.next = next;
		return head;
		
	}
	
	public static void main(String[] args) {
		Node head = new Node();
		head.data = 0;
		head.appendToTail(1);
		head.appendToTail(2);
		head.appendToTail(3);
		head.appendToTail(4);
		head.appendToTail(5);
		head = InsertNth(head, 7, 2);
	}
}

public class linked_list {
	

}


