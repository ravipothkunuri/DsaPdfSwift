#!/usr/bin/env python3
"""
DSA Problems PDF Generator
Creates a comprehensive PDF containing Data Structures and Algorithms problems
with Swift solutions, explanations, and complexity analysis.
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Preformatted
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
import io
import re
from datetime import datetime

class DSAProblemsPDFGenerator:
    def __init__(self):
        self.doc = SimpleDocTemplate("DSA_Problems_Swift_Solutions.pdf", pagesize=A4)
        self.styles = getSampleStyleSheet()
        self.story = []
        self.setup_custom_styles()
        
    def setup_custom_styles(self):
        """Set up custom styles for the PDF."""
        # Title style
        self.title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue
        )
        
        # Problem title style
        self.problem_title_style = ParagraphStyle(
            'ProblemTitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            spaceBefore=20,
            textColor=colors.darkgreen
        )
        
        # Section header style
        self.section_style = ParagraphStyle(
            'SectionHeader',
            parent=self.styles['Heading3'],
            fontSize=14,
            spaceAfter=8,
            spaceBefore=12,
            textColor=colors.darkred
        )
        
        # Code style for Preformatted text
        self.code_style = self.create_code_style()
        
        # Complexity style
        self.complexity_style = ParagraphStyle(
            'ComplexityStyle',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.blue,
            fontName='Helvetica-Bold'
        )

    def add_title_page(self):
        """Add the title page to the PDF."""
        self.story.append(Spacer(1, 2*inch))
        
        title = Paragraph("Data Structures & Algorithms<br/>Problems and Solutions", self.title_style)
        self.story.append(title)
        self.story.append(Spacer(1, 0.5*inch))
        
        subtitle = Paragraph("Complete Swift Implementation Guide", self.styles['Heading2'])
        self.story.append(subtitle)
        self.story.append(Spacer(1, 0.3*inch))
        
        date_text = f"Generated on: {datetime.now().strftime('%B %d, %Y')}"
        date_para = Paragraph(date_text, self.styles['Normal'])
        self.story.append(date_para)
        
        self.story.append(PageBreak())

    def add_table_of_contents(self):
        """Add table of contents."""
        toc_title = Paragraph("Table of Contents", self.problem_title_style)
        self.story.append(toc_title)
        
        toc_data = [
            ["1. Array Problems", "Page 3"],
            ["   • Two Sum", ""],
            ["   • Maximum Subarray", ""],
            ["   • Merge Sorted Arrays", ""],
            ["2. Linked List Problems", "Page 8"],
            ["   • Reverse Linked List", ""],
            ["   • Merge Two Sorted Lists", ""],
            ["   • Detect Cycle", ""],
            ["3. Tree Problems", "Page 13"],
            ["   • Binary Tree Traversal", ""],
            ["   • Maximum Depth", ""],
            ["   • Validate BST", ""],
            ["4. Graph Problems", "Page 18"],
            ["   • Breadth-First Search", ""],
            ["   • Depth-First Search", ""],
            ["   • Shortest Path", ""],
        ]
        
        toc_table = Table(toc_data, colWidths=[4*inch, 1*inch])
        toc_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        
        self.story.append(toc_table)
        self.story.append(PageBreak())

    def add_problem(self, category, title, description, swift_solution, time_complexity, space_complexity, explanation=""):
        """Add a problem with its Swift solution to the PDF."""
        # Problem title
        problem_header = Paragraph(f"{category}: {title}", self.problem_title_style)
        self.story.append(problem_header)
        
        # Problem description
        desc_header = Paragraph("Problem Description:", self.section_style)
        self.story.append(desc_header)
        desc_para = Paragraph(description, self.styles['Normal'])
        self.story.append(desc_para)
        self.story.append(Spacer(1, 12))
        
        # Swift solution
        solution_header = Paragraph("Swift Solution:", self.section_style)
        self.story.append(solution_header)
        
        # Use Preformatted for proper code display
        code_block = Preformatted(swift_solution, self.code_style)
        self.story.append(code_block)
        
        # Explanation
        if explanation:
            exp_header = Paragraph("Explanation:", self.section_style)
            self.story.append(exp_header)
            exp_para = Paragraph(explanation, self.styles['Normal'])
            self.story.append(exp_para)
            self.story.append(Spacer(1, 12))
        
        # Complexity analysis
        complexity_header = Paragraph("Complexity Analysis:", self.section_style)
        self.story.append(complexity_header)
        
        time_para = Paragraph(f"<b>Time Complexity:</b> {time_complexity}", self.complexity_style)
        space_para = Paragraph(f"<b>Space Complexity:</b> {space_complexity}", self.complexity_style)
        self.story.append(time_para)
        self.story.append(space_para)
        
        self.story.append(Spacer(1, 20))

    def create_code_style(self):
        """Create a proper code style for Preformatted text."""
        return ParagraphStyle(
            'CodePreformatted',
            fontName='Courier',
            fontSize=9,
            backgroundColor=colors.lightgrey,
            borderWidth=1,
            borderColor=colors.grey,
            leftIndent=20,
            rightIndent=20,
            spaceAfter=12,
            spaceBefore=6,
            leading=12
        )

    def generate_problems(self):
        """Generate all DSA problems with Swift solutions."""
        
        # Array Problems
        category_header = Paragraph("Array Problems", self.title_style)
        self.story.append(category_header)
        self.story.append(Spacer(1, 20))
        
        # Two Sum Problem
        two_sum_code = '''func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    var numToIndex: [Int: Int] = [:]
    
    for (index, num) in nums.enumerated() {
        let complement = target - num
        
        if let complementIndex = numToIndex[complement] {
            return [complementIndex, index]
        }
        
        numToIndex[num] = index
    }
    
    return [] // No solution found
}

// Example usage:
let nums = [2, 7, 11, 15]
let target = 9
let result = twoSum(nums, target)
print(result) // Output: [0, 1]'''

        self.add_problem(
            "Array",
            "Two Sum",
            "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.",
            two_sum_code,
            "O(n)",
            "O(n)",
            "We use a hash map to store each number and its index as we iterate through the array. For each number, we calculate its complement (target - current number) and check if it exists in our hash map. If found, we return the indices."
        )
        
        # Maximum Subarray
        max_subarray_code = '''func maxSubArray(_ nums: [Int]) -> Int {
    guard !nums.isEmpty else { return 0 }
    
    var maxSum = nums[0]
    var currentSum = nums[0]
    
    for i in 1..<nums.count {
        currentSum = max(nums[i], currentSum + nums[i])
        maxSum = max(maxSum, currentSum)
    }
    
    return maxSum
}

// Example usage:
let nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
let result = maxSubArray(nums)
print(result) // Output: 6 (subarray [4, -1, 2, 1])'''

        self.add_problem(
            "Array",
            "Maximum Subarray (Kadane's Algorithm)",
            "Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.",
            max_subarray_code,
            "O(n)",
            "O(1)",
            "Kadane's algorithm maintains the maximum sum ending at each position. At each step, we decide whether to extend the existing subarray or start a new one from the current element."
        )
        
        # Merge Sorted Arrays
        merge_arrays_code = '''func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
    var i = m - 1  // Last element in nums1
    var j = n - 1  // Last element in nums2
    var k = m + n - 1  // Last position in nums1
    
    // Merge from the end to avoid overwriting
    while i >= 0 && j >= 0 {
        if nums1[i] > nums2[j] {
            nums1[k] = nums1[i]
            i -= 1
        } else {
            nums1[k] = nums2[j]
            j -= 1
        }
        k -= 1
    }
    
    // Copy remaining elements from nums2
    while j >= 0 {
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    }
}

// Example usage:
var nums1 = [1, 2, 3, 0, 0, 0]
let nums2 = [2, 5, 6]
merge(&nums1, 3, nums2, 3)
print(nums1) // Output: [1, 2, 2, 3, 5, 6]'''

        self.add_problem(
            "Array",
            "Merge Sorted Arrays",
            "You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.",
            merge_arrays_code,
            "O(m + n)",
            "O(1)",
            "We merge from the end of both arrays to avoid overwriting elements in nums1. This allows us to merge in-place without extra space."
        )
        
        self.story.append(PageBreak())
        
        # Linked List Problems
        category_header = Paragraph("Linked List Problems", self.title_style)
        self.story.append(category_header)
        self.story.append(Spacer(1, 20))
        
        # Linked List Node Definition and Reverse
        reverse_list_code = '''class ListNode {
    var val: Int
    var next: ListNode?
    
    init(_ val: Int) {
        self.val = val
        self.next = nil
    }
}

func reverseList(_ head: ListNode?) -> ListNode? {
    var prev: ListNode? = nil
    var current = head
    
    while current != nil {
        let nextTemp = current?.next
        current?.next = prev
        prev = current
        current = nextTemp
    }
    
    return prev
}

// Recursive approach:
func reverseListRecursive(_ head: ListNode?) -> ListNode? {
    guard let head = head, let next = head.next else {
        return head
    }
    
    let reversedList = reverseListRecursive(next)
    next.next = head
    head.next = nil
    
    return reversedList
}'''

        self.add_problem(
            "Linked List",
            "Reverse Linked List",
            "Given the head of a singly linked list, reverse the list, and return the reversed list.",
            reverse_list_code,
            "O(n)",
            "O(1) iterative, O(n) recursive",
            "The iterative approach uses three pointers to reverse the links. The recursive approach reverses the rest of the list first, then fixes the current connection."
        )
        
        # Merge Two Sorted Lists
        merge_lists_code = '''func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
    let dummy = ListNode(0)
    var current = dummy
    var l1 = list1
    var l2 = list2
    
    while l1 != nil && l2 != nil {
        if l1!.val <= l2!.val {
            current.next = l1
            l1 = l1!.next
        } else {
            current.next = l2
            l2 = l2!.next
        }
        current = current.next!
    }
    
    // Append remaining nodes
    current.next = l1 ?? l2
    
    return dummy.next
}

// Example usage:
// list1: 1 -> 2 -> 4
// list2: 1 -> 3 -> 4
// result: 1 -> 1 -> 2 -> 3 -> 4 -> 4'''

        self.add_problem(
            "Linked List",
            "Merge Two Sorted Lists",
            "You are given the heads of two sorted linked lists list1 and list2. Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.",
            merge_lists_code,
            "O(m + n)",
            "O(1)",
            "We use a dummy node to simplify the logic and iterate through both lists, always choosing the smaller value. Finally, we append any remaining nodes."
        )
        
        # Detect Cycle
        detect_cycle_code = '''func hasCycle(_ head: ListNode?) -> Bool {
    var slow = head
    var fast = head
    
    while fast != nil && fast?.next != nil {
        slow = slow?.next
        fast = fast?.next?.next
        
        if slow === fast {
            return true
        }
    }
    
    return false
}

// Finding the start of the cycle
func detectCycle(_ head: ListNode?) -> ListNode? {
    var slow = head
    var fast = head
    
    // First, detect if there's a cycle
    while fast != nil && fast?.next != nil {
        slow = slow?.next
        fast = fast?.next?.next
        
        if slow === fast {
            break
        }
    }
    
    // No cycle found
    if fast == nil || fast?.next == nil {
        return nil
    }
    
    // Find the start of the cycle
    slow = head
    while slow !== fast {
        slow = slow?.next
        fast = fast?.next
    }
    
    return slow
}'''

        self.add_problem(
            "Linked List",
            "Detect Cycle",
            "Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.",
            detect_cycle_code,
            "O(n)",
            "O(1)",
            "Floyd's Cycle Detection Algorithm (Tortoise and Hare): Use two pointers moving at different speeds. If there's a cycle, the fast pointer will eventually meet the slow pointer."
        )
        
        # Binary Tree Problems
        self.story.append(PageBreak())
        category_header = Paragraph("Binary Tree Problems", self.title_style)
        self.story.append(category_header)
        self.story.append(Spacer(1, 20))
        
        tree_traversal_code = '''class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    
    init(_ val: Int) {
        self.val = val
        self.left = nil
        self.right = nil
    }
}

// Inorder Traversal
func inorderTraversal(_ root: TreeNode?) -> [Int] {
    var result: [Int] = []
    
    func inorder(_ node: TreeNode?) {
        guard let node = node else { return }
        
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    }
    
    inorder(root)
    return result
}

// Iterative approach using stack
func inorderTraversalIterative(_ root: TreeNode?) -> [Int] {
    var result: [Int] = []
    var stack: [TreeNode] = []
    var current = root
    
    while current != nil || !stack.isEmpty {
        while current != nil {
            stack.append(current!)
            current = current!.left
        }
        
        current = stack.removeLast()
        result.append(current!.val)
        current = current!.right
    }
    
    return result
}'''

        self.add_problem(
            "Binary Tree",
            "Binary Tree Inorder Traversal",
            "Given the root of a binary tree, return the inorder traversal of its nodes' values. (Left, Root, Right)",
            tree_traversal_code,
            "O(n)",
            "O(h) where h is height of tree",
            "Inorder traversal visits left subtree, then root, then right subtree. The recursive approach is natural, while the iterative approach uses a stack to simulate the recursion."
        )
        
        # Maximum Depth of Binary Tree
        max_depth_code = '''func maxDepth(_ root: TreeNode?) -> Int {
    guard let root = root else { return 0 }
    
    let leftDepth = maxDepth(root.left)
    let rightDepth = maxDepth(root.right)
    
    return max(leftDepth, rightDepth) + 1
}

// Iterative approach using level-order traversal
func maxDepthIterative(_ root: TreeNode?) -> Int {
    guard let root = root else { return 0 }
    
    var queue: [TreeNode] = [root]
    var depth = 0
    
    while !queue.isEmpty {
        let levelSize = queue.count
        depth += 1
        
        for _ in 0..<levelSize {
            let node = queue.removeFirst()
            
            if let left = node.left {
                queue.append(left)
            }
            if let right = node.right {
                queue.append(right)
            }
        }
    }
    
    return depth
}'''

        self.add_problem(
            "Binary Tree",
            "Maximum Depth of Binary Tree",
            "Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.",
            max_depth_code,
            "O(n)",
            "O(h) recursive, O(w) iterative where h is height and w is width",
            "The recursive approach calculates depth by finding the maximum of left and right subtree depths plus 1. The iterative approach uses level-order traversal to count levels."
        )
        
        # Validate Binary Search Tree
        validate_bst_code = '''func isValidBST(_ root: TreeNode?) -> Bool {
    return validate(root, nil, nil)
}

func validate(_ node: TreeNode?, _ minVal: Int?, _ maxVal: Int?) -> Bool {
    guard let node = node else { return true }
    
    // Check if current node violates BST property
    if let minVal = minVal, node.val <= minVal { return false }
    if let maxVal = maxVal, node.val >= maxVal { return false }
    
    // Recursively validate left and right subtrees
    return validate(node.left, minVal, node.val) && 
           validate(node.right, node.val, maxVal)
}

// Alternative approach using inorder traversal
func isValidBSTInorder(_ root: TreeNode?) -> Bool {
    var prev: Int? = nil
    
    func inorder(_ node: TreeNode?) -> Bool {
        guard let node = node else { return true }
        
        if !inorder(node.left) { return false }
        
        if let prevVal = prev, node.val <= prevVal {
            return false
        }
        prev = node.val
        
        return inorder(node.right)
    }
    
    return inorder(root)
}'''

        self.add_problem(
            "Binary Tree",
            "Validate Binary Search Tree",
            "Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows: The left subtree of a node contains only nodes with keys less than the node's key. The right subtree of a node contains only nodes with keys greater than the node's key. Both the left and right subtrees must also be binary search trees.",
            validate_bst_code,
            "O(n)",
            "O(h) where h is the height of the tree",
            "We can validate by maintaining min/max bounds for each node, or by doing inorder traversal and checking if the result is sorted."
        )
        
        # Stack and Queue Problems
        self.story.append(PageBreak())
        category_header = Paragraph("Stack and Queue Problems", self.title_style)
        self.story.append(category_header)
        self.story.append(Spacer(1, 20))
        
        # Valid Parentheses (Stack)
        valid_parentheses_code = '''func isValid(_ s: String) -> Bool {
    var stack: [Character] = []
    let pairs: [Character: Character] = [")": "(", "}": "{", "]": "["]
    
    for char in s {
        if pairs.keys.contains(char) {
            // Closing bracket
            if stack.isEmpty || stack.removeLast() != pairs[char] {
                return false
            }
        } else {
            // Opening bracket
            stack.append(char)
        }
    }
    
    return stack.isEmpty
}

// Example usage:
print(isValid("()"))        // true
print(isValid("()[]{}"))    // true
print(isValid("(]"))        // false
print(isValid("([)]"))      // false'''

        self.add_problem(
            "Stack",
            "Valid Parentheses",
            "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order.",
            valid_parentheses_code,
            "O(n)",
            "O(n)",
            "Use a stack to keep track of opening brackets. When we encounter a closing bracket, check if it matches the most recent opening bracket."
        )
        
        # Implement Queue using Stacks
        queue_using_stacks_code = '''class MyQueue {
    private var inStack: [Int] = []
    private var outStack: [Int] = []
    
    init() {}
    
    func push(_ x: Int) {
        inStack.append(x)
    }
    
    func pop() -> Int {
        peek()
        return outStack.removeLast()
    }
    
    func peek() -> Int {
        if outStack.isEmpty {
            while !inStack.isEmpty {
                outStack.append(inStack.removeLast())
            }
        }
        return outStack.last!
    }
    
    func empty() -> Bool {
        return inStack.isEmpty && outStack.isEmpty
    }
}

// Example usage:
let queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  // 1
print(queue.pop())   // 1
print(queue.empty()) // false'''

        self.add_problem(
            "Queue",
            "Implement Queue using Stacks",
            "Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).",
            queue_using_stacks_code,
            "O(1) amortized for all operations",
            "O(n)",
            "Use two stacks: one for input and one for output. Transfer elements from input to output stack only when output stack is empty."
        )
        
        # Graph Problems
        self.story.append(PageBreak())
        category_header = Paragraph("Graph Problems", self.title_style)
        self.story.append(category_header)
        self.story.append(Spacer(1, 20))
        
        # Graph representation and BFS
        bfs_code = '''// Graph represented as adjacency list
func bfs(_ graph: [Int: [Int]], start: Int) -> [Int] {
    var visited: Set<Int> = []
    var queue: [Int] = [start]
    var result: [Int] = []
    
    visited.insert(start)
    
    while !queue.isEmpty {
        let node = queue.removeFirst()
        result.append(node)
        
        if let neighbors = graph[node] {
            for neighbor in neighbors {
                if !visited.contains(neighbor) {
                    visited.insert(neighbor)
                    queue.append(neighbor)
                }
            }
        }
    }
    
    return result
}

// Example usage:
let graph = [
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
]
let bfsResult = bfs(graph, start: 2)
print(bfsResult) // [2, 0, 3, 1]'''

        self.add_problem(
            "Graph",
            "Breadth-First Search (BFS)",
            "Implement breadth-first search traversal for a graph. BFS explores all vertices at the present depth prior to moving on to vertices at the next depth level.",
            bfs_code,
            "O(V + E)",
            "O(V)",
            "BFS uses a queue to process nodes level by level. We mark nodes as visited to avoid cycles and process all neighbors before moving to the next level."
        )
        
        # DFS
        dfs_code = '''func dfs(_ graph: [Int: [Int]], start: Int) -> [Int] {
    var visited: Set<Int> = []
    var result: [Int] = []
    
    func dfsHelper(_ node: Int) {
        visited.insert(node)
        result.append(node)
        
        if let neighbors = graph[node] {
            for neighbor in neighbors {
                if !visited.contains(neighbor) {
                    dfsHelper(neighbor)
                }
            }
        }
    }
    
    dfsHelper(start)
    return result
}

// Iterative DFS using stack
func dfsIterative(_ graph: [Int: [Int]], start: Int) -> [Int] {
    var visited: Set<Int> = []
    var stack: [Int] = [start]
    var result: [Int] = []
    
    while !stack.isEmpty {
        let node = stack.removeLast()
        
        if !visited.contains(node) {
            visited.insert(node)
            result.append(node)
            
            if let neighbors = graph[node] {
                for neighbor in neighbors.reversed() {
                    if !visited.contains(neighbor) {
                        stack.append(neighbor)
                    }
                }
            }
        }
    }
    
    return result
}'''

        self.add_problem(
            "Graph",
            "Depth-First Search (DFS)",
            "Implement depth-first search traversal for a graph. DFS explores as far as possible along each branch before backtracking.",
            dfs_code,
            "O(V + E)",
            "O(V)",
            "DFS can be implemented recursively or iteratively using a stack. We explore each path completely before backtracking to explore other paths."
        )
        
        # Shortest Path (Dijkstra's simplified)
        shortest_path_code = '''// Simplified shortest path using BFS for unweighted graphs
func shortestPath(_ graph: [Int: [Int]], start: Int, end: Int) -> [Int]? {
    var queue: [(Int, [Int])] = [(start, [start])]
    var visited: Set<Int> = [start]
    
    while !queue.isEmpty {
        let (node, path) = queue.removeFirst()
        
        if node == end {
            return path
        }
        
        if let neighbors = graph[node] {
            for neighbor in neighbors {
                if !visited.contains(neighbor) {
                    visited.insert(neighbor)
                    queue.append((neighbor, path + [neighbor]))
                }
            }
        }
    }
    
    return nil // No path found
}

// Example usage:
let graph = [
    0: [1, 2],
    1: [2, 3],
    2: [3],
    3: []
]
if let path = shortestPath(graph, start: 0, end: 3) {
    print("Shortest path: \\(path)") // [0, 1, 3] or [0, 2, 3]
}'''

        self.add_problem(
            "Graph",
            "Shortest Path (Unweighted)",
            "Find the shortest path between two nodes in an unweighted graph. Return the path as a list of nodes from start to end.",
            shortest_path_code,
            "O(V + E)",
            "O(V)",
            "For unweighted graphs, BFS naturally finds the shortest path since it explores nodes level by level, guaranteeing the first path found is the shortest."
        )

    def generate_pdf(self):
        """Generate the complete PDF."""
        print("Starting PDF generation...")
        
        # Add title page
        self.add_title_page()
        
        # Add table of contents
        self.add_table_of_contents()
        
        # Generate all problems
        self.generate_problems()
        
        # Build the PDF
        self.doc.build(self.story)
        print(f"PDF generated successfully: DSA_Problems_Swift_Solutions.pdf")
        return "DSA_Problems_Swift_Solutions.pdf"

def main():
    """Main function to generate the DSA problems PDF."""
    generator = DSAProblemsPDFGenerator()
    pdf_filename = generator.generate_pdf()
    
    print(f"✅ Successfully generated: {pdf_filename}")
    print("📄 The PDF contains DSA problems with Swift solutions, explanations, and complexity analysis.")
    
if __name__ == "__main__":
    main()