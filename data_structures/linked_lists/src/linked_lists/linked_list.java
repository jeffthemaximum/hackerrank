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
		

		Node curr, newNode, next;
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
	
	public static Node deleteNode(Node head, int position) {
		if (head == null) {
			return null;
		}
		
		Node n = head;
		if (position == 0) {
			return head.next;
		}
		
		int count = 0;
		
		while (n.next != null) {
			if (count == (position - 1)) {
				n.next = n.next.next;
				return head;
			}
			n = n.next;
			count += 1;
		}
		return head;

	}
	
	static void reversePrint(Node head) {
		if (head.next == null) {
			System.out.println(head.data);
		}
		
		//reverse list
		Node prev, curr, next;
		prev = null;
		curr = head;
		while (curr != null) {
			next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;
		}
		//print list
		while (prev != null) {
			System.out.println(prev.data);
			prev = prev.next;
		}
	}
	
	/*
	  Compare two linked lists A and B
	  Return 1 if they are identical and 0 if they are not. 
	  Node is defined as 
	  class Node {
	     int data;
	     Node next;
	  }
	*/
	int CompareLists(Node headA, Node headB) {
	    if (headA == null && headB == null) {
	    	return 1;
	    }
	    
	    //check that all data are equal
	    while (headA != null && headB != null) {
	    	if (headA.data != headB.data) {
	    		return 0;
	    	}
	    	headA = headA.next;
	    	headB = headB.next;
	    }
	    
	    //check that lengths are equal
	    if (headA != null || headB != null) {
	    	return 0;
	    }
	    
	    return 1;
	    
	  
	}
	
	public static void main(String[] args) {
		Node head = new Node();
		head.data = 0;
		head.appendToTail(1);
		head.appendToTail(2);
		head.appendToTail(3);
		head.appendToTail(4);
		head.appendToTail(5);
		//head = InsertNth(head, 7, 2);
		reversePrint(head);
	}
	
}

public class linked_list {
	

}


