class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        Deque<Integer> deque = new LinkedList<>();
        Stack<Integer> stack = new Stack<>();
        int served = 0;

        for (int student: students) {
            deque.add(student);
        } 

        for (int i = sandwiches.length - 1; i >= 0; i--) {
            stack.push(sandwiches[i]);
        }

        while (served < deque.size() && !stack.isEmpty()) {
            if (stack.peek() == deque.peekFirst()) {
                stack.pop();
                deque.pollFirst();
                served = 0;
            } else {
                deque.addLast(deque.peekFirst());
                deque.pollFirst();
                served++;
            }

        }
        return deque.size();
        
    }
}