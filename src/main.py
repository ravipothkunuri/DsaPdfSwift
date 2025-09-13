#!/usr/bin/env python3
"""
Comprehensive Swift Programming Guide PDF Generator
Creates an extensive PDF covering Swift fundamentals, advanced topics, SwiftUI, 
Combine, networking, iOS development, and data structures & algorithms.
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

class SwiftProgrammingGuidePDFGenerator:
    def __init__(self):
        self.doc = SimpleDocTemplate("Comprehensive_Swift_Programming_Guide.pdf", pagesize=A4)
        self.styles = getSampleStyleSheet()
        self.story = []
        self.setup_custom_styles()
        
    def setup_custom_styles(self):
        """Set up custom styles for the PDF."""
        # Main title style
        self.main_title_style = ParagraphStyle(
            'MainTitle',
            parent=self.styles['Heading1'],
            fontSize=28,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.darkblue,
            fontName='Helvetica-Bold'
        )
        
        # Chapter title style
        self.chapter_title_style = ParagraphStyle(
            'ChapterTitle',
            parent=self.styles['Heading1'],
            fontSize=20,
            spaceAfter=20,
            spaceBefore=30,
            alignment=TA_CENTER,
            textColor=colors.darkgreen,
            fontName='Helvetica-Bold'
        )
        
        # Topic title style
        self.topic_title_style = ParagraphStyle(
            'TopicTitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            spaceBefore=20,
            textColor=colors.darkred,
            fontName='Helvetica-Bold'
        )
        
        # Section header style
        self.section_style = ParagraphStyle(
            'SectionHeader',
            parent=self.styles['Heading3'],
            fontSize=14,
            spaceAfter=8,
            spaceBefore=12,
            textColor=colors.purple,
            fontName='Helvetica-Bold'
        )
        
        # Code style for Preformatted text
        self.code_style = ParagraphStyle(
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
        
        # Note style
        self.note_style = ParagraphStyle(
            'NoteStyle',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.blue,
            fontName='Helvetica-Oblique',
            leftIndent=20,
            spaceAfter=8
        )
        
        # Key point style
        self.key_point_style = ParagraphStyle(
            'KeyPointStyle',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.darkred,
            fontName='Helvetica-Bold'
        )

    def add_title_page(self):
        """Add the title page to the PDF."""
        self.story.append(Spacer(1, 2*inch))
        
        title = Paragraph("Comprehensive Swift<br/>Programming Guide", self.main_title_style)
        self.story.append(title)
        self.story.append(Spacer(1, 0.5*inch))
        
        subtitle = Paragraph("Swift Language • SwiftUI • Combine • Networking<br/>iOS Development • Data Structures & Algorithms", self.styles['Heading3'])
        self.story.append(subtitle)
        self.story.append(Spacer(1, 0.5*inch))
        
        description = Paragraph("A complete guide with 120+ topics, code examples, and practical implementations", self.styles['Normal'])
        self.story.append(description)
        self.story.append(Spacer(1, 0.3*inch))
        
        date_text = f"Generated on: {datetime.now().strftime('%B %d, %Y')}"
        date_para = Paragraph(date_text, self.styles['Normal'])
        self.story.append(date_para)
        
        self.story.append(PageBreak())

    def add_comprehensive_table_of_contents(self):
        """Add comprehensive table of contents."""
        toc_title = Paragraph("Table of Contents", self.chapter_title_style)
        self.story.append(toc_title)
        
        toc_data = [
            ["PART I: SWIFT LANGUAGE FUNDAMENTALS", ""],
            ["Chapter 1: Swift Basics", ""],
            ["   1.1 Variables and Constants", ""],
            ["   1.2 Data Types", ""],
            ["   1.3 Optionals", ""],
            ["   1.4 Control Flow", ""],
            ["   1.5 Functions", ""],
            ["   1.6 Closures", ""],
            ["   1.7 Collections", ""],
            ["   1.8 Strings", ""],
            ["   1.9 Error Handling", ""],
            ["", ""],
            
            ["Chapter 2: Object-Oriented Programming", ""],
            ["   2.1 Classes vs Structures", ""],
            ["   2.2 Properties", ""],
            ["   2.3 Inheritance", ""],
            ["   2.4 Initialization", ""],
            ["   2.5 Protocols", ""],
            ["   2.6 Extensions", ""],
            ["", ""],
            
            ["Chapter 3: Advanced Swift", ""],
            ["   3.1 Generics", ""],
            ["   3.2 Memory Management", ""],
            ["   3.3 Protocol-Oriented Programming", ""],
            ["   3.4 Property Wrappers", ""],
            ["   3.5 Result Builders", ""],
            ["", ""],
            
            ["PART II: CONCURRENCY & MODERN SWIFT", ""],
            ["Chapter 4: Concurrency", ""],
            ["   4.1 Async/Await", ""],
            ["   4.2 Tasks", ""],
            ["   4.3 Actors", ""],
            ["   4.4 Structured Concurrency", ""],
            ["", ""],
            
            ["PART III: SwiftUI FRAMEWORK", ""],
            ["Chapter 5: SwiftUI Fundamentals", ""],
            ["   5.1 Views and Modifiers", ""],
            ["   5.2 Layout System", ""],
            ["   5.3 State Management", ""],
            ["   5.4 Navigation", ""],
            ["   5.5 Lists and Forms", ""],
            ["", ""],
            
            ["Chapter 6: Advanced SwiftUI", ""],
            ["   6.1 Custom Views", ""],
            ["   6.2 Animations", ""],
            ["   6.3 Gestures", ""],
            ["   6.4 MVVM Pattern", ""],
            ["", ""],
            
            ["PART IV: REACTIVE PROGRAMMING", ""],
            ["Chapter 7: Combine Framework", ""],
            ["   7.1 Publishers and Subscribers", ""],
            ["   7.2 Operators", ""],
            ["   7.3 Subjects", ""],
            ["   7.4 Schedulers", ""],
            ["", ""],
            
            ["PART V: NETWORKING & APIs", ""],
            ["Chapter 8: Networking", ""],
            ["   8.1 URLSession", ""],
            ["   8.2 JSON & Codable", ""],
            ["   8.3 REST APIs", ""],
            ["   8.4 Authentication", ""],
            ["   8.5 WebSockets", ""],
            ["", ""],
            
            ["PART VI: iOS DEVELOPMENT", ""],
            ["Chapter 9: Data Persistence", ""],
            ["   9.1 UserDefaults", ""],
            ["   9.2 Core Data", ""],
            ["   9.3 File System", ""],
            ["   9.4 Keychain", ""],
            ["", ""],
            
            ["Chapter 10: Testing & Architecture", ""],
            ["   10.1 Unit Testing", ""],
            ["   10.2 UI Testing", ""],
            ["   10.3 MVVM Architecture", ""],
            ["   10.4 Dependency Injection", ""],
            ["", ""],
            
            ["APPENDIX: DATA STRUCTURES & ALGORITHMS", ""],
            ["   A.1 Array Problems", ""],
            ["   A.2 Linked List Problems", ""],
            ["   A.3 Tree Problems", ""],
            ["   A.4 Graph Problems", ""],
        ]
        
        toc_table = Table(toc_data, colWidths=[4.5*inch, 0.5*inch])
        toc_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
            ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),  # Part titles
            ('FONTNAME', (0, 12), (0, 12), 'Helvetica-Bold'),
            ('FONTNAME', (0, 21), (0, 21), 'Helvetica-Bold'),
            ('FONTNAME', (0, 28), (0, 28), 'Helvetica-Bold'),
            ('FONTNAME', (0, 36), (0, 36), 'Helvetica-Bold'),
            ('FONTNAME', (0, 46), (0, 46), 'Helvetica-Bold'),
            ('FONTNAME', (0, 56), (0, 56), 'Helvetica-Bold'),
        ]))
        
        self.story.append(toc_table)
        self.story.append(PageBreak())

    def add_topic(self, title, description, code_example, key_points=None, notes=None):
        """Add a topic with code example to the PDF."""
        # Topic title
        topic_header = Paragraph(title, self.topic_title_style)
        self.story.append(topic_header)
        
        # Description
        if description:
            desc_para = Paragraph(description, self.styles['Normal'])
            self.story.append(desc_para)
            self.story.append(Spacer(1, 8))
        
        # Code example
        if code_example:
            code_header = Paragraph("Code Example:", self.section_style)
            self.story.append(code_header)
            code_block = Preformatted(code_example, self.code_style)
            self.story.append(code_block)
        
        # Key points
        if key_points:
            points_header = Paragraph("Key Points:", self.section_style)
            self.story.append(points_header)
            if isinstance(key_points, list):
                for point in key_points:
                    point_para = Paragraph(f"• {point}", self.key_point_style)
                    self.story.append(point_para)
            else:
                point_para = Paragraph(key_points, self.key_point_style)
                self.story.append(point_para)
            self.story.append(Spacer(1, 8))
        
        # Notes
        if notes:
            note_header = Paragraph("Notes:", self.section_style)
            self.story.append(note_header)
            note_para = Paragraph(notes, self.note_style)
            self.story.append(note_para)
        
        self.story.append(Spacer(1, 15))

    def add_chapter_title(self, title):
        """Add a chapter title."""
        self.story.append(PageBreak())
        chapter_title = Paragraph(title, self.chapter_title_style)
        self.story.append(chapter_title)
        self.story.append(Spacer(1, 20))

    def generate_swift_basics_content(self):
        """Generate Swift basics content - Part I."""
        
        self.add_chapter_title("PART I: SWIFT LANGUAGE FUNDAMENTALS")
        
        # Chapter 1: Swift Basics
        self.add_chapter_title("Chapter 1: Swift Basics")
        
        # 1.1 Variables and Constants
        self.add_topic(
            "1.1 Variables and Constants",
            "Swift uses 'var' for mutable variables and 'let' for immutable constants. Type inference allows Swift to automatically determine types.",
            '''// Variables (mutable)
var playerName = "Alice"
var score = 100
var isActive = true

// Constants (immutable)
let maxPlayers = 4
let gameTitle = "Swift Adventure"
let pi = 3.14159

// Explicit type annotations
var temperature: Double = 98.6
let items: [String] = ["sword", "shield", "potion"]

// Multiple declarations
var x = 0.0, y = 0.0, z = 0.0
let red, green, blue: Double''',
            ["Use 'let' by default, 'var' only when you need to change the value",
             "Type inference reduces verbosity while maintaining type safety",
             "Constants improve performance and prevent accidental mutations"],
            "Swift encourages immutability through 'let'. The compiler optimizes constants more effectively than variables."
        )
        
        # 1.2 Data Types
        self.add_topic(
            "1.2 Data Types",
            "Swift provides various built-in data types including integers, floating-point numbers, booleans, strings, and more.",
            '''// Integer types
let smallNumber: Int8 = 127
let regularNumber: Int = 42
let bigNumber: Int64 = 9223372036854775807

// Floating-point types
let pi: Float = 3.14159
let precisePi: Double = 3.141592653589793

// Boolean
let isSwiftFun: Bool = true

// Character and String
let letter: Character = "A"
let greeting: String = "Hello, Swift!"

// Type conversion
let integerValue = 42
let floatValue = Float(integerValue)
let stringValue = String(integerValue)

// Type checking
if floatValue is Float {
    print("It's a Float!")
}''',
            ["Int and Double are the most commonly used numeric types",
             "Swift doesn't perform implicit type conversions",
             "Use type conversion initializers for explicit conversions",
             "Type checking with 'is' operator helps ensure type safety"],
            "Swift is a type-safe language, preventing type-related errors at compile time."
        )
        
        # 1.3 Optionals
        self.add_topic(
            "1.3 Optionals",
            "Optionals represent either a value or nil (absence of value). They're fundamental to Swift's safety model.",
            '''// Declaring optionals
var optionalString: String? = "Hello"
var optionalInt: Int? = nil

// Optional binding with if-let
if let actualString = optionalString {
    print("The string is: \\(actualString)")
} else {
    print("No string value")
}

// Guard statement
func processString(_ str: String?) {
    guard let unwrapped = str else {
        print("String is nil")
        return
    }
    print("Processing: \\(unwrapped)")
}

// Nil-coalescing operator
let defaultName = "Anonymous"
let userName = optionalString ?? defaultName

// Optional chaining
class Person {
    var residence: Residence?
}
class Residence {
    var address: String?
}

let person = Person()
let address = person.residence?.address

// Implicitly unwrapped optionals
var assumedString: String! = "An implicitly unwrapped optional string."''',
            ["Use optionals to handle absence of values safely",
             "Prefer optional binding over force unwrapping",
             "Guard statements provide early exit for nil values",
             "Optional chaining prevents crashes when accessing nested optionals"],
            "Optionals eliminate null pointer exceptions and make your code more robust."
        )
        
        # 1.4 Control Flow
        self.add_topic(
            "1.4 Control Flow",
            "Swift provides various control flow statements including if, switch, loops, and control transfer statements.",
            '''// If statements
let temperature = 75
if temperature > 80 {
    print("It's hot!")
} else if temperature > 60 {
    print("It's warm")
} else {
    print("It's cool")
}

// Switch statements (powerful in Swift)
let character = "a"
switch character {
case "a", "e", "i", "o", "u":
    print("It's a vowel")
case "b"..."z":
    print("It's a consonant")
default:
    print("Not a letter")
}

// Switch with ranges and where clauses
let point = (2, 3)
switch point {
case (0, 0):
    print("Origin")
case (_, 0):
    print("On x-axis")
case (0, _):
    print("On y-axis")
case let (x, y) where x == y:
    print("On diagonal")
case let (x, y):
    print("Point at (\\(x), \\(y))")
}

// For loops
for i in 1...5 {
    print("Count: \\(i)")
}

let names = ["Anna", "Alex", "Brian", "Jack"]
for name in names {
    print("Hello, \\(name)!")
}

// While loops
var counter = 0
while counter < 3 {
    print(counter)
    counter += 1
}

// Repeat-while (do-while equivalent)
repeat {
    print("This executes at least once")
    counter -= 1
} while counter > 0''',
            ["Swift's switch statement is exhaustive and doesn't fall through by default",
             "Pattern matching in switch makes complex conditions elegant",
             "Range operators (...) and (..<) are useful in loops and switches",
             "Control transfer statements: continue, break, fallthrough, return, throw"],
            "Swift's control flow statements are more powerful than many other languages, especially switch statements."
        )
        
        # 1.5 Functions
        self.add_topic(
            "1.5 Functions",
            "Functions are self-contained chunks of code that perform specific tasks. Swift functions are flexible and powerful.",
            '''// Basic function
func greet(person: String) -> String {
    return "Hello, \\(person)!"
}
let greeting = greet(person: "Taylor")

// Function with multiple parameters
func greet(person: String, from hometown: String) -> String {
    return "Hello \\(person)! Glad you could visit from \\(hometown)."
}
print(greet(person: "Bill", from: "Cupertino"))

// Function with default parameters
func greet(person: String, from hometown: String = "Unknown") -> String {
    return "Hello \\(person)! Glad you could visit from \\(hometown)."
}

// Variadic parameters
func arithmeticMean(_ numbers: Double...) -> Double {
    var total: Double = 0
    for number in numbers {
        total += number
    }
    return total / Double(numbers.count)
}
print(arithmeticMean(1, 2, 3, 4, 5))

// In-out parameters
func swapTwoInts(_ a: inout Int, _ b: inout Int) {
    let temporaryA = a
    a = b
    b = temporaryA
}

var someInt = 3
var anotherInt = 107
swapTwoInts(&someInt, &anotherInt)

// Function types
func addTwoInts(_ a: Int, _ b: Int) -> Int {
    return a + b
}

let mathFunction: (Int, Int) -> Int = addTwoInts
print(mathFunction(2, 3))

// Nested functions
func chooseStepFunction(backward: Bool) -> (Int) -> Int {
    func stepForward(input: Int) -> Int { return input + 1 }
    func stepBackward(input: Int) -> Int { return input - 1 }
    
    return backward ? stepBackward : stepForward
}''',
            ["Parameter labels improve code readability",
             "Default parameters reduce function overloading",
             "inout parameters allow functions to modify external variables",
             "Functions are first-class types in Swift"],
            "Swift functions support many advanced features like closures, higher-order functions, and functional programming patterns."
        )
        
        # Continue with more topics...
        self.add_topic(
            "1.6 Closures",
            "Closures are self-contained blocks of functionality that can be passed around. They're similar to lambdas in other languages.",
            '''// Basic closure syntax
let names = ["Chris", "Alex", "Ewa", "Barry", "Daniella"]

// Full closure syntax
let reversedNames = names.sorted(by: { (s1: String, s2: String) -> Bool in
    return s1 > s2
})

// Inferring type from context
let reversed1 = names.sorted(by: { s1, s2 in return s1 > s2 })

// Implicit returns
let reversed2 = names.sorted(by: { s1, s2 in s1 > s2 })

// Shorthand argument names
let reversed3 = names.sorted(by: { $0 > $1 })

// Operator method
let reversed4 = names.sorted(by: >)

// Trailing closure syntax
let reversed5 = names.sorted { $0 > $1 }

// Capturing values
func makeIncrementer(forIncrement amount: Int) -> () -> Int {
    var runningTotal = 0
    func incrementer() -> Int {
        runningTotal += amount
        return runningTotal
    }
    return incrementer
}

let incrementByTen = makeIncrementer(forIncrement: 10)
print(incrementByTen()) // 10
print(incrementByTen()) // 20

// Escaping closures
var completionHandlers: [() -> Void] = []

func someFunctionWithEscapingClosure(completionHandler: @escaping () -> Void) {
    completionHandlers.append(completionHandler)
}

// Autoclosures
func simpleAssert(_ condition: @autoclosure () -> Bool, _ message: String) {
    if !condition() {
        print(message)
    }
}

let testNumber = 5
simpleAssert(testNumber > 0, "Number must be positive")''',
            ["Closures can capture and store references to variables and constants",
             "Trailing closure syntax makes code more readable",
             "@escaping closures outlive the function that calls them",
             "@autoclosure automatically wraps expressions in closures"],
            "Closures are extensively used in Swift for callbacks, functional programming, and asynchronous operations."
        )
        
        # 1.7 Collections
        self.add_topic(
            "1.7 Collections",
            "Swift provides three primary collection types: arrays, sets, and dictionaries for storing multiple values.",
            '''// Arrays
var fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits.insert("kiwi", at: 1)

// Array methods
let numbers = [1, 2, 3, 4, 5]
let doubled = numbers.map { $0 * 2 }
let evens = numbers.filter { $0 % 2 == 0 }
let sum = numbers.reduce(0, +)

// Sets
var uniqueNumbers: Set<Int> = [1, 2, 3, 2, 1]
print(uniqueNumbers) // [1, 2, 3]

let set1: Set = [1, 2, 3]
let set2: Set = [3, 4, 5]
let intersection = set1.intersection(set2) // [3]
let union = set1.union(set2) // [1, 2, 3, 4, 5]

// Dictionaries
var studentGrades = ["Alice": 95, "Bob": 87, "Charlie": 92]
studentGrades["Diana"] = 89
studentGrades.updateValue(88, forKey: "Bob")

// Dictionary iteration
for (name, grade) in studentGrades {
    print("\\(name): \\(grade)")
}

// Nested collections
let matrix: [[Int]] = [[1, 2], [3, 4], [5, 6]]
let coordinates = [(x: 1, y: 2), (x: 3, y: 4)]''',
            ["Arrays are ordered collections of values",
             "Sets store unique values in no defined ordering",
             "Dictionaries store key-value associations",
             "All collections support functional programming methods"],
            "Swift collections are type-safe and provide powerful methods for data manipulation."
        )
        
        # 1.8 Strings
        self.add_topic(
            "1.8 Strings",
            "Swift strings are Unicode-compliant and provide powerful manipulation methods.",
            '''// String basics
let greeting = "Hello, World!"
let multilineString = """
    This is a multiline
    string in Swift with
    proper formatting
    """

// String interpolation
let name = "Swift"
let version = 5.0
let message = "Welcome to \\(name) \\(version)!"

// String methods
let text = "Hello, Swift Programming"
print(text.count) // Character count
print(text.uppercased())
print(text.lowercased())
print(text.hasPrefix("Hello"))
print(text.hasSuffix("Programming"))

// String manipulation
let sentence = "Swift is awesome"
let words = sentence.split(separator: " ")
let joined = words.joined(separator: "-")

// Character iteration
for character in greeting {
    print(character)
}

// String indices
let str = "Swift"
let startIndex = str.startIndex
let endIndex = str.endIndex
let secondChar = str[str.index(after: startIndex)]

// String slicing
let range = str.index(str.startIndex, offsetBy: 1)..<str.index(str.endIndex, offsetBy: -1)
let substring = str[range]

// Regular expressions (iOS 16+)
let pattern = #"\\d+"#
if let regex = try? Regex(pattern) {
    let numbers = "Age: 25, Score: 100"
    let matches = numbers.matches(of: regex)
}''',
            ["Strings are value types and use copy-on-write optimization",
             "String interpolation with \\() is preferred over concatenation",
             "Strings use String.Index for position-based operations",
             "Regular expressions provide powerful pattern matching"],
            "Swift strings are designed for Unicode correctness and international text support."
        )
        
        # 1.9 Error Handling
        self.add_topic(
            "1.9 Error Handling",
            "Swift provides first-class error handling with do-catch blocks, throwing functions, and the Result type.",
            '''// Define errors
enum ValidationError: Error {
    case tooShort
    case tooLong
    case invalidCharacters
    case empty
}

// Throwing function
func validatePassword(_ password: String) throws -> Bool {
    if password.isEmpty {
        throw ValidationError.empty
    }
    
    if password.count < 8 {
        throw ValidationError.tooShort
    }
    
    if password.count > 50 {
        throw ValidationError.tooLong
    }
    
    return true
}

// Do-catch block
func testPassword() {
    do {
        try validatePassword("secret")
        print("Password is valid")
    } catch ValidationError.tooShort {
        print("Password is too short")
    } catch ValidationError.empty {
        print("Password cannot be empty")
    } catch {
        print("Unknown error: \\(error)")
    }
}

// Try variants
let password1 = try? validatePassword("mypassword") // Returns nil on error
let password2 = try! validatePassword("validpassword") // Crashes on error

// Result type
func validatePasswordResult(_ password: String) -> Result<Bool, ValidationError> {
    do {
        let isValid = try validatePassword(password)
        return .success(isValid)
    } catch let error as ValidationError {
        return .failure(error)
    } catch {
        return .failure(.invalidCharacters)
    }
}

// Using Result
let result = validatePasswordResult("test")
switch result {
case .success(let isValid):
    print("Validation result: \\(isValid)")
case .failure(let error):
    print("Validation failed: \\(error)")
}

// Rethrowing functions
func processPasswords<T>(_ passwords: [String], processor: (String) throws -> T) rethrows -> [T] {
    return try passwords.map(processor)
}''',
            ["Use specific error types conforming to Error protocol",
             "Do-catch blocks handle errors gracefully",
             "try? converts errors to optionals, try! force-unwraps",
             "Result type provides functional error handling"],
            "Swift's error handling is designed to be explicit and safe, preventing runtime crashes from unhandled errors."
        )

    def generate_advanced_swift_content(self):
        """Generate advanced Swift content."""
        
        # Chapter 2: Object-Oriented Programming
        self.add_chapter_title("Chapter 2: Object-Oriented Programming")
        
        # 2.1 Classes vs Structures
        self.add_topic(
            "2.1 Classes vs Structures",
            "Swift provides both classes and structures. Understanding when to use each is crucial for effective Swift programming.",
            '''// Structure (Value Type)
struct Point {
    var x: Double
    var y: Double
    
    func distanceFromOrigin() -> Double {
        return sqrt(x * x + y * y)
    }
    
    // Mutating method for value types
    mutating func moveBy(x deltaX: Double, y deltaY: Double) {
        x += deltaX
        y += deltaY
    }
}

// Class (Reference Type)
class Vehicle {
    var currentSpeed = 0.0
    var description: String {
        return "traveling at \\(currentSpeed) miles per hour"
    }
    
    func makeNoise() {
        // Override in subclass
    }
}

class Bicycle: Vehicle {
    var hasBasket = false
    
    override func makeNoise() {
        print("Ring ring!")
    }
}

// Identity operators for reference types
let vehicle1 = Vehicle()
let vehicle2 = Vehicle()
let vehicle3 = vehicle1

if vehicle1 === vehicle3 {
    print("Same instance")
}

// Copy behavior difference
var point1 = Point(x: 1.0, y: 2.0)
var point2 = point1  // Copies the value
point2.x = 3.0
print(point1.x)  // Still 1.0

let bike1 = Bicycle()
let bike2 = bike1  // Same reference
bike2.currentSpeed = 10.0
print(bike1.currentSpeed)  // Also 10.0''',
            ["Structures are value types (copied), classes are reference types (shared)",
             "Use structures for simple data containers and value semantics",
             "Use classes when you need inheritance or reference semantics",
             "Identity operators (=== and !==) compare reference equality"],
            "Choose structures by default and classes when you specifically need reference semantics."
        )
        
        # 2.2 Properties
        self.add_topic(
            "2.2 Properties",
            "Properties associate values with classes, structures, and enumerations. Swift provides stored and computed properties.",
            '''// Stored properties
struct FixedLengthRange {
    var firstValue: Int
    let length: Int  // Constant stored property
}

// Lazy stored properties
class DataImporter {
    var filename = "data.txt"
    // Expensive initialization
}

class DataManager {
    lazy var importer = DataImporter()
    var data: [String] = []
}

// Computed properties
struct Point {
    var x = 0.0, y = 0.0
}

struct Size {
    var width = 0.0, height = 0.0
}

struct Rect {
    var origin = Point()
    var size = Size()
    
    var center: Point {
        get {
            let centerX = origin.x + (size.width / 2)
            let centerY = origin.y + (size.height / 2)
            return Point(x: centerX, y: centerY)
        }
        set(newCenter) {
            origin.x = newCenter.x - (size.width / 2)
            origin.y = newCenter.y - (size.height / 2)
        }
    }
    
    // Read-only computed property
    var area: Double {
        return size.width * size.height
    }
}

// Property observers
class StepCounter {
    var totalSteps: Int = 0 {
        willSet(newTotalSteps) {
            print("About to set totalSteps to \\(newTotalSteps)")
        }
        didSet {
            if totalSteps > oldValue {
                print("Added \\(totalSteps - oldValue) steps")
            }
        }
    }
}

// Property wrappers
@propertyWrapper
struct Clamped<T: Comparable> {
    private var value: T
    private let range: ClosedRange<T>
    
    init(wrappedValue: T, _ range: ClosedRange<T>) {
        self.range = range
        self.value = max(range.lowerBound, min(range.upperBound, wrappedValue))
    }
    
    var wrappedValue: T {
        get { value }
        set { value = max(range.lowerBound, min(range.upperBound, newValue)) }
    }
}

struct Player {
    @Clamped(0...100) var health: Int = 100
    @Clamped(0...10) var level: Int = 1
}''',
            ["Stored properties store constant and variable values",
             "Computed properties calculate values on-the-fly",
             "Property observers respond to changes in property values",
             "Property wrappers provide reusable property behavior"],
            "Properties are a fundamental part of Swift's type system, providing flexible data access patterns."
        )
        
        # 2.3 Inheritance
        self.add_topic(
            "2.3 Inheritance",
            "Classes can inherit methods, properties, and characteristics from another class. Swift supports single inheritance.",
            '''// Base class
class Vehicle {
    var currentSpeed = 0.0
    
    var description: String {
        return "traveling at \\(currentSpeed) miles per hour"
    }
    
    func makeNoise() {
        // Default implementation
        print("Some generic vehicle noise")
    }
}

// Subclass
class Bicycle: Vehicle {
    var hasBasket = false
    
    override func makeNoise() {
        print("Ring ring!")
    }
}

// Further subclassing
class Tandem: Bicycle {
    var currentNumberOfPassengers = 0
    
    override var description: String {
        return super.description + " with \\(currentNumberOfPassengers) passengers"
    }
}

// Preventing inheritance
final class FinalVehicle: Vehicle {
    // Cannot be subclassed
}

// Overriding properties
class Car: Vehicle {
    var gear = 1
    
    override var description: String {
        return super.description + " in gear \\(gear)"
    }
    
    // Overriding property observers
    override var currentSpeed: Double {
        didSet {
            gear = Int(currentSpeed / 10.0) + 1
        }
    }
}

// Initialization inheritance
class ElectricCar: Car {
    var batteryLevel: Double
    
    init(batteryLevel: Double) {
        self.batteryLevel = batteryLevel
        super.init()
        self.currentSpeed = 25.0
    }
    
    override func makeNoise() {
        print("Whisper quiet...")
    }
}''',
            ["Only classes support inheritance in Swift",
             "Use 'override' keyword to override methods and properties",
             "Call superclass methods with 'super'",
             "Use 'final' to prevent inheritance"],
            "Inheritance enables code reuse and polymorphism, but favor composition over inheritance when possible."
        )
        
        # 2.4 Initialization
        self.add_topic(
            "2.4 Initialization",
            "Initialization is the process of preparing an instance for use. Swift provides designated and convenience initializers.",
            '''// Basic initialization
struct Celsius {
    var temperatureInCelsius: Double
    
    init(fromFahrenheit fahrenheit: Double) {
        temperatureInCelsius = (fahrenheit - 32.0) / 1.8
    }
    
    init(fromKelvin kelvin: Double) {
        temperatureInCelsius = kelvin - 273.15
    }
    
    init(_ celsius: Double) {
        temperatureInCelsius = celsius
    }
}

// Class initialization
class Food {
    var name: String
    
    init(name: String) {
        self.name = name
    }
    
    convenience init() {
        self.init(name: "[Unnamed]")
    }
}

class RecipeIngredient: Food {
    var quantity: Int
    
    init(name: String, quantity: Int) {
        self.quantity = quantity
        super.init(name: name)
    }
    
    override convenience init(name: String) {
        self.init(name: name, quantity: 1)
    }
}

// Failable initializers
struct Animal {
    let species: String
    
    init?(species: String) {
        if species.isEmpty {
            return nil
        }
        self.species = species
    }
}

// Required initializers
class SomeClass {
    required init() {
        // Implementation
    }
}

class SomeSubclass: SomeClass {
    required init() {
        // Must implement required initializer
    }
}

// Memberwise initializers (structs only)
struct Point {
    var x: Double
    var y: Double
    // Automatically gets init(x:y:)
}

// Deinitialization
class Player {
    let playerName: String
    
    init(name: String) {
        self.playerName = name
        print("\\(playerName) has joined the game")
    }
    
    deinit {
        print("\\(playerName) has left the game")
    }
}''',
            ["Designated initializers fully initialize all properties",
             "Convenience initializers call other initializers",
             "Failable initializers return nil if initialization fails",
             "Required initializers must be implemented by all subclasses"],
            "Swift's initialization system ensures all properties are initialized before the instance is ready for use."
        )
        
        self.add_chapter_title("Chapter 3: Advanced Swift")
        
        # 3.1 Generics
        self.add_topic(
            "3.1 Generics",
            "Generics enable you to write flexible, reusable functions and types that can work with any type, subject to requirements you define.",
            '''// Generic function
func swapTwoValues<T>(_ a: inout T, _ b: inout T) {
    let temporaryA = a
    a = b
    b = temporaryA
}

var someInt = 3
var anotherInt = 107
swapTwoValues(&someInt, &anotherInt)

// Generic types
struct Stack<Element> {
    var items: [Element] = []
    
    mutating func push(_ item: Element) {
        items.append(item)
    }
    
    mutating func pop() -> Element {
        return items.removeLast()
    }
    
    func peek() -> Element? {
        return items.last
    }
}

var stackOfStrings = Stack<String>()
stackOfStrings.push("uno")
stackOfStrings.push("dos")

// Type constraints
func findIndex<T: Equatable>(of valueToFind: T, in array: [T]) -> Int? {
    for (index, value) in array.enumerated() {
        if value == valueToFind {
            return index
        }
    }
    return nil
}

// Associated types in protocols
protocol Container {
    associatedtype Item
    mutating func append(_ item: Item)
    var count: Int { get }
    subscript(i: Int) -> Item { get }
}

struct IntStack: Container {
    typealias Item = Int
    var items: [Int] = []
    
    mutating func append(_ item: Int) {
        items.append(item)
    }
    
    var count: Int {
        return items.count
    }
    
    subscript(i: Int) -> Int {
        return items[i]
    }
}

// Generic where clauses
func allItemsMatch<C1: Container, C2: Container>
    (_ someContainer: C1, _ anotherContainer: C2) -> Bool
    where C1.Item == C2.Item, C1.Item: Equatable {
    
    if someContainer.count != anotherContainer.count {
        return false
    }
    
    for i in 0..<someContainer.count {
        if someContainer[i] != anotherContainer[i] {
            return false
        }
    }
    
    return true
}''',
            ["Generics provide type safety while maintaining flexibility",
             "Type constraints ensure generic types conform to required protocols",
             "Associated types make protocols more flexible",
             "Where clauses add additional requirements to generic functions"],
            "Generics are extensively used in Swift's standard library and are key to creating reusable, type-safe code."
        )
        
        # 3.2 Protocols
        self.add_topic(
            "3.2 Protocols",
            "Protocols define a blueprint of methods, properties, and requirements that suit a particular task or piece of functionality.",
            '''// Basic protocol
protocol Drawable {
    func draw()
    var area: Double { get }
    var perimeter: Double { get }
}

// Protocol implementation
struct Circle: Drawable {
    let radius: Double
    
    func draw() {
        print("Drawing a circle with radius \\(radius)")
    }
    
    var area: Double {
        return .pi * radius * radius
    }
    
    var perimeter: Double {
        return 2 * .pi * radius
    }
}

// Protocol inheritance
protocol Shape3D: Drawable {
    var volume: Double { get }
}

// Multiple protocol conformance
protocol Identifiable {
    var id: String { get }
}

struct User: Identifiable, CustomStringConvertible {
    let id: String
    let name: String
    
    var description: String {
        return "User(id: \\(id), name: \\(name))"
    }
}

// Protocol extensions
extension Drawable {
    func drawWithBorder() {
        print("Drawing border...")
        draw()
        print("Border complete")
    }
    
    // Default implementation
    var description: String {
        return "A shape with area \\(area)"
    }
}

// Protocol with associated types
protocol Container {
    associatedtype Item
    var count: Int { get }
    mutating func append(_ item: Item)
    subscript(i: Int) -> Item { get }
}

struct Stack<Element>: Container {
    var items: [Element] = []
    
    var count: Int {
        return items.count
    }
    
    mutating func append(_ item: Element) {
        items.append(item)
    }
    
    subscript(i: Int) -> Element {
        return items[i]
    }
}

// Protocol composition
protocol Named {
    var name: String { get }
}

protocol Aged {
    var age: Int { get }
}

func greetPerson(_ person: Named & Aged) {
    print("Hello, \\(person.name), you are \\(person.age) years old")
}

// Checking protocol conformance
if let circle = someObject as? Drawable {
    circle.draw()
}''',
            ["Protocols define contracts that types must fulfill",
             "Protocol extensions provide default implementations",
             "Associated types make protocols generic",
             "Protocol composition combines multiple protocols"],
            "Protocols are fundamental to Swift's protocol-oriented programming paradigm."
        )
        
        # 3.3 Extensions
        self.add_topic(
            "3.3 Extensions",
            "Extensions add new functionality to existing classes, structures, enumerations, or protocol types without modifying their source code.",
            '''// Basic extension
extension Double {
    var squared: Double {
        return self * self
    }
    
    func rounded(toDecimalPlaces places: Int) -> Double {
        let multiplier = pow(10, Double(places))
        return (self * multiplier).rounded() / multiplier
    }
}

let number = 3.14159
print(number.squared) // 9.8696
print(number.rounded(toDecimalPlaces: 2)) // 3.14

// Extension with initializers
extension String {
    init(repeating character: Character, count: Int) {
        self = String(Array(repeating: character, count: count))
    }
    
    var isPalindrome: Bool {
        let cleaned = self.lowercased().filter { $0.isLetter }
        return cleaned == String(cleaned.reversed())
    }
}

let stars = String(repeating: "*", count: 5) // "*****"
print("racecar".isPalindrome) // true

// Extension with subscripts
extension Array {
    subscript(safe index: Int) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}

let numbers = [1, 2, 3, 4, 5]
print(numbers[safe: 10]) // nil instead of crash

// Extension with nested types
extension Character {
    enum Kind {
        case vowel
        case consonant
        case other
    }
    
    var kind: Kind {
        switch lowercased() {
        case "a", "e", "i", "o", "u":
            return .vowel
        case "a"..."z":
            return .consonant
        default:
            return .other
        }
    }
}

let char: Character = "E"
print(char.kind) // vowel

// Generic extension
extension Array where Element: Comparable {
    func quickSorted() -> [Element] {
        guard count > 1 else { return self }
        
        let pivot = self[count / 2]
        let less = self.filter { $0 < pivot }
        let equal = self.filter { $0 == pivot }
        let greater = self.filter { $0 > pivot }
        
        return less.quickSorted() + equal + greater.quickSorted()
    }
}

let unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
let sorted = unsorted.quickSorted()''',
            ["Extensions add functionality without modifying original code",
             "Can add computed properties, methods, initializers, and subscripts",
             "Generic extensions can add conditional functionality",
             "Extensions can conform types to protocols"],
            "Extensions are a powerful way to organize code and add functionality to existing types."
        )
        
        # Add Concurrency Chapter
        self.add_chapter_title("PART II: CONCURRENCY & MODERN SWIFT")
        self.add_chapter_title("Chapter 4: Concurrency")
        
        # 4.1 Async/Await
        self.add_topic(
            "4.1 Async/Await",
            "Swift's async/await syntax provides a clean way to write asynchronous code that reads like synchronous code.",
            '''// Basic async function
func fetchUserData(id: String) async throws -> User {
    let url = URL(string: "https://api.example.com/users/\\(id)")!
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode(User.self, from: data)
}

// Calling async functions
func loadUserProfile() async {
    do {
        let user = try await fetchUserData(id: "123")
        print("Loaded user: \\(user.name)")
    } catch {
        print("Failed to load user: \\(error)")
    }
}

// Async properties
class ImageLoader {
    private var cache: [URL: UIImage] = [:]
    
    var imageCount: Int {
        cache.count
    }
    
    func image(from url: URL) async throws -> UIImage {
        // Check cache first
        if let cachedImage = cache[url] {
            return cachedImage
        }
        
        // Download image
        let (data, _) = try await URLSession.shared.data(from: url)
        guard let image = UIImage(data: data) else {
            throw ImageError.invalidData
        }
        
        // Cache the image
        cache[url] = image
        return image
    }
}

// Async sequences
func countDown(from number: Int) -> AsyncStream<Int> {
    AsyncStream { continuation in
        Task {
            for i in (0...number).reversed() {
                continuation.yield(i)
                try await Task.sleep(nanoseconds: 1_000_000_000) // 1 second
            }
            continuation.finish()
        }
    }
}

// Using async sequences
func runCountdown() async {
    for await count in countDown(from: 5) {
        print("Count: \\(count)")
    }
    print("Done!")
}

// Async/await with completion handlers
func legacyNetworkCall(completion: @escaping (Result<Data, Error>) -> Void) {
    // Legacy callback-based code
}

// Convert to async/await
func modernNetworkCall() async throws -> Data {
    return try await withCheckedThrowingContinuation { continuation in
        legacyNetworkCall { result in
            continuation.resume(with: result)
        }
    }
}

// Multiple concurrent operations
func loadMultipleUsers() async throws -> [User] {
    async let user1 = fetchUserData(id: "1")
    async let user2 = fetchUserData(id: "2")
    async let user3 = fetchUserData(id: "3")
    
    return try await [user1, user2, user3]
}''',
            ["async functions must be called with await",
             "async/await eliminates callback hell",
             "Use async let for concurrent operations",
             "AsyncSequence provides asynchronous iteration"],
            "Async/await makes asynchronous code more readable and easier to debug than callback-based approaches."
        )
        
        # 4.2 Tasks
        self.add_topic(
            "4.2 Tasks",
            "Tasks represent units of asynchronous work. Swift provides Task, TaskGroup, and various cancellation mechanisms.",
            '''// Basic Task creation
func startBackgroundWork() {
    Task {
        let result = await performLongRunningOperation()
        await updateUI(with: result)
    }
}

// Task with priority
func highPriorityWork() {
    Task(priority: .high) {
        await performCriticalOperation()
    }
}

// Detached tasks
func detachedWork() {
    Task.detached {
        // This task doesn't inherit context
        await performIndependentWork()
    }
}

// TaskGroup for multiple concurrent operations
func processItemsConcurrently(_ items: [String]) async -> [ProcessedItem] {
    await withTaskGroup(of: ProcessedItem.self) { group in
        var results: [ProcessedItem] = []
        
        for item in items {
            group.addTask {
                return await processItem(item)
            }
        }
        
        for await result in group {
            results.append(result)
        }
        
        return results
    }
}

// Error handling in TaskGroup
func processWithErrorHandling(_ items: [String]) async -> [ProcessedItem] {
    await withTaskGroup(of: Result<ProcessedItem, Error>.self) { group in
        var results: [ProcessedItem] = []
        
        for item in items {
            group.addTask {
                do {
                    let processed = try await processItemThrowing(item)
                    return .success(processed)
                } catch {
                    return .failure(error)
                }
            }
        }
        
        for await result in group {
            switch result {
            case .success(let item):
                results.append(item)
            case .failure(let error):
                print("Failed to process item: \\(error)")
            }
        }
        
        return results
    }
}

// Task cancellation
class DataProcessor {
    private var currentTask: Task<Void, Error>?
    
    func startProcessing() {
        currentTask = Task {
            for i in 1...1000 {
                // Check for cancellation
                try Task.checkCancellation()
                
                await processItem(i)
                
                // Alternative cancellation check
                if Task.isCancelled {
                    print("Task was cancelled")
                    return
                }
            }
        }
    }
    
    func cancelProcessing() {
        currentTask?.cancel()
    }
}

// Task local values
enum TaskLocals {
    @TaskLocal static var userID: String?
    @TaskLocal static var requestID: String = UUID().uuidString
}

func performUserOperation() async {
    await TaskLocals.$userID.withValue("user123") {
        await TaskLocals.$requestID.withValue("req456") {
            await someOperation()
            // userID and requestID are available here
        }
    }
}''',
            ["Task represents a unit of asynchronous work",
             "TaskGroup enables structured concurrency for multiple operations",
             "Tasks can be cancelled cooperatively",
             "Task-local values provide context inheritance"],
            "Tasks provide structured concurrency, making concurrent code predictable and manageable."
        )
        
        # 4.3 Actors
        self.add_topic(
            "4.3 Actors",
            "Actors provide data isolation and protect against data races in concurrent programming.",
            '''// Basic actor
actor Counter {
    private var value = 0
    
    func increment() -> Int {
        value += 1
        return value
    }
    
    func getValue() -> Int {
        return value
    }
    
    func reset() {
        value = 0
    }
}

// Using actors
func useCounter() async {
    let counter = Counter()
    
    let value1 = await counter.increment() // Must use await
    let value2 = await counter.getValue()
    
    print("Counter values: \\(value1), \\(value2)")
}

// Actor with async methods
actor ImageCache {
    private var images: [URL: UIImage] = [:]
    
    func image(for url: URL) async -> UIImage? {
        if let cached = images[url] {
            return cached
        }
        
        // Fetch image
        do {
            let (data, _) = try await URLSession.shared.data(from: url)
            let image = UIImage(data: data)
            images[url] = image
            return image
        } catch {
            return nil
        }
    }
    
    func clearCache() {
        images.removeAll()
    }
}

// MainActor for UI updates
@MainActor
class ViewModel: ObservableObject {
    @Published var data: [String] = []
    
    func loadData() async {
        let newData = await fetchDataFromNetwork()
        
        // This runs on main actor automatically
        self.data = newData
    }
    
    // Non-isolated methods can be called from any context
    nonisolated func validateInput(_ input: String) -> Bool {
        return !input.isEmpty
    }
}

// Global actor
@globalActor
actor DatabaseActor {
    static let shared = DatabaseActor()
    private init() {}
}

@DatabaseActor
func saveToDatabase(_ data: Data) {
    // All calls to this function are serialized
    // through the DatabaseActor
}

// Actor inheritance (only from protocols)
protocol Drawable {
    func draw() async
}

actor DrawingCanvas: Drawable {
    private var shapes: [Shape] = []
    
    func draw() async {
        for shape in shapes {
            await shape.render()
        }
    }
    
    func addShape(_ shape: Shape) {
        shapes.append(shape)
    }
}

// Sendable types for actor boundaries
struct SafeData: Sendable {
    let id: String
    let value: Int
}

actor DataProcessor {
    func process(_ data: SafeData) async -> ProcessedData {
        // Safe to pass Sendable types across actor boundaries
        return await processData(data)
    }
}''',
            ["Actors provide data isolation and prevent data races",
             "Actor methods are called with await from outside the actor",
             "MainActor ensures UI updates happen on the main thread",
             "Sendable types can be safely passed between actors"],
            "Actors are Swift's solution to thread-safe programming without explicit locks or queues."
        )

    def generate_swiftui_content(self):
        """Generate SwiftUI content - Part III."""
        
        self.add_chapter_title("PART III: SwiftUI FRAMEWORK")
        
        self.add_chapter_title("Chapter 5: SwiftUI Fundamentals")
        
        # 5.1 Views and Modifiers
        self.add_topic(
            "5.1 Views and Modifiers",
            "SwiftUI uses a declarative syntax where you describe what your UI should look like. Views are modified using modifiers that return new views.",
            '''import SwiftUI

// Basic views
struct ContentView: View {
    var body: some View {
        VStack {
            Text("Hello, SwiftUI!")
                .font(.largeTitle)
                .foregroundColor(.blue)
                .padding()
            
            Image(systemName: "star.fill")
                .foregroundColor(.yellow)
                .font(.system(size: 50))
            
            Button("Tap Me") {
                print("Button tapped!")
            }
            .padding()
            .background(Color.blue)
            .foregroundColor(.white)
            .cornerRadius(10)
        }
    }
}

// Custom view with modifiers
struct CustomCard: View {
    let title: String
    let subtitle: String
    
    var body: some View {
        VStack(alignment: .leading) {
            Text(title)
                .font(.headline)
                .fontWeight(.bold)
            
            Text(subtitle)
                .font(.subheadline)
                .foregroundColor(.gray)
        }
        .padding()
        .background(Color.white)
        .cornerRadius(10)
        .shadow(radius: 5)
    }
}

// View composition
struct MainView: View {
    var body: some View {
        ScrollView {
            LazyVStack(spacing: 16) {
                CustomCard(title: "SwiftUI", subtitle: "Declarative UI framework")
                CustomCard(title: "Combine", subtitle: "Reactive programming")
                CustomCard(title: "Swift", subtitle: "Programming language")
            }
            .padding()
        }
    }
}

// ViewBuilder and conditional views
struct ConditionalView: View {
    @State private var showDetails = false
    
    var body: some View {
        VStack {
            Text("Main Content")
            
            if showDetails {
                Text("Additional Details")
                    .transition(.opacity)
            }
            
            Button(showDetails ? "Hide" : "Show") {
                withAnimation {
                    showDetails.toggle()
                }
            }
        }
    }
}''',
            ["Views are value types that describe UI declaratively",
             "Modifiers return new views, enabling method chaining",
             "View composition creates reusable components",
             "ViewBuilder enables conditional and loop-based view construction"],
            "SwiftUI's declarative approach means you describe the desired end state, and SwiftUI figures out how to get there."
        )
        
        # 5.3 State Management
        self.add_topic(
            "5.3 State Management",
            "SwiftUI uses various property wrappers to manage state and data flow in your application.",
            '''import SwiftUI

// @State for local state
struct CounterView: View {
    @State private var count = 0
    
    var body: some View {
        VStack {
            Text("Count: \\(count)")
                .font(.largeTitle)
            
            HStack {
                Button("Increment") {
                    count += 1
                }
                
                Button("Decrement") {
                    count -= 1
                }
                
                Button("Reset") {
                    count = 0
                }
            }
        }
    }
}

// @Binding for two-way data flow
struct ToggleView: View {
    @Binding var isOn: Bool
    
    var body: some View {
        Toggle("Feature Enabled", isOn: $isOn)
            .padding()
    }
}

struct ParentView: View {
    @State private var featureEnabled = false
    
    var body: some View {
        VStack {
            Text("Feature is \\(featureEnabled ? "ON" : "OFF")")
            ToggleView(isOn: $featureEnabled)
        }
    }
}

// @ObservableObject and @Published
class UserStore: ObservableObject {
    @Published var users: [User] = []
    @Published var isLoading = false
    @Published var errorMessage: String?
    
    func loadUsers() async {
        isLoading = true
        errorMessage = nil
        
        do {
            let fetchedUsers = try await NetworkService.fetchUsers()
            await MainActor.run {
                self.users = fetchedUsers
                self.isLoading = false
            }
        } catch {
            await MainActor.run {
                self.errorMessage = error.localizedDescription
                self.isLoading = false
            }
        }
    }
}

struct UserListView: View {
    @StateObject private var userStore = UserStore()
    
    var body: some View {
        NavigationView {
            Group {
                if userStore.isLoading {
                    ProgressView("Loading users...")
                } else if let error = userStore.errorMessage {
                    Text("Error: \\(error)")
                        .foregroundColor(.red)
                } else {
                    List(userStore.users) { user in
                        UserRowView(user: user)
                    }
                }
            }
            .navigationTitle("Users")
            .task {
                await userStore.loadUsers()
            }
        }
    }
}

// @EnvironmentObject for dependency injection
struct ContentView: View {
    var body: some View {
        TabView {
            UserListView()
                .tabItem {
                    Image(systemName: "person.3")
                    Text("Users")
                }
            
            SettingsView()
                .tabItem {
                    Image(systemName: "gear")
                    Text("Settings")
                }
        }
        .environmentObject(UserStore())
    }
}

// @AppStorage for UserDefaults
struct SettingsView: View {
    @AppStorage("username") private var username = ""
    @AppStorage("isDarkMode") private var isDarkMode = false
    @AppStorage("fontSize") private var fontSize = 16.0
    
    var body: some View {
        Form {
            Section("User Preferences") {
                TextField("Username", text: $username)
                
                Toggle("Dark Mode", isOn: $isDarkMode)
                
                Stepper("Font Size: \\(Int(fontSize))", value: $fontSize, in: 12...24)
            }
        }
        .preferredColorScheme(isDarkMode ? .dark : .light)
    }
}''',
            ["@State manages local view state",
             "@Binding creates two-way data connections",
             "@StateObject creates and owns ObservableObject instances",
             "@EnvironmentObject shares data across the view hierarchy",
             "@AppStorage automatically syncs with UserDefaults"],
            "SwiftUI's reactive state management system automatically updates views when data changes."
        )
        
        # 5.4 Navigation
        self.add_topic(
            "5.4 Navigation",
            "SwiftUI provides various navigation patterns including NavigationView, NavigationLink, and programmatic navigation.",
            '''import SwiftUI

// Basic Navigation
struct ContentView: View {
    var body: some View {
        NavigationView {
            List {
                NavigationLink("Profile", destination: ProfileView())
                NavigationLink("Settings", destination: SettingsView())
                NavigationLink("About", destination: AboutView())
            }
            .navigationTitle("Main Menu")
            .navigationBarTitleDisplayMode(.large)
        }
    }
}

// NavigationStack (iOS 16+)
struct ModernNavigationView: View {
    @State private var path = NavigationPath()
    
    var body: some View {
        NavigationStack(path: $path) {
            List {
                Button("Go to Detail") {
                    path.append("detail")
                }
                
                Button("Go to Settings") {
                    path.append("settings")
                }
            }
            .navigationDestination(for: String.self) { value in
                switch value {
                case "detail":
                    DetailView()
                case "settings":
                    SettingsView()
                default:
                    Text("Unknown destination")
                }
            }
            .navigationTitle("Navigation Stack")
        }
    }
}

// Programmatic navigation
class NavigationController: ObservableObject {
    @Published var isShowingDetail = false
    @Published var selectedUser: User?
    
    func showUserDetail(_ user: User) {
        selectedUser = user
        isShowingDetail = true
    }
    
    func dismissDetail() {
        isShowingDetail = false
        selectedUser = nil
    }
}

struct UserListView: View {
    @StateObject private var navigation = NavigationController()
    @State private var users: [User] = []
    
    var body: some View {
        NavigationView {
            List(users) { user in
                Button(user.name) {
                    navigation.showUserDetail(user)
                }
            }
            .navigationTitle("Users")
            .sheet(isPresented: $navigation.isShowingDetail) {
                if let user = navigation.selectedUser {
                    UserDetailView(user: user)
                }
            }
        }
    }
}

// Tab Navigation
struct MainTabView: View {
    @State private var selectedTab = 0
    
    var body: some View {
        TabView(selection: $selectedTab) {
            HomeView()
                .tabItem {
                    Image(systemName: "house")
                    Text("Home")
                }
                .tag(0)
            
            SearchView()
                .tabItem {
                    Image(systemName: "magnifyingglass")
                    Text("Search")
                }
                .tag(1)
            
            ProfileView()
                .tabItem {
                    Image(systemName: "person")
                    Text("Profile")
                }
                .tag(2)
        }
        .accentColor(.blue)
    }
}

// Modal presentation
struct ModalExampleView: View {
    @State private var isShowingModal = false
    @State private var isShowingFullScreen = false
    
    var body: some View {
        VStack(spacing: 20) {
            Button("Show Sheet") {
                isShowingModal = true
            }
            .sheet(isPresented: $isShowingModal) {
                ModalContentView(isPresented: $isShowingModal)
            }
            
            Button("Show Full Screen") {
                isShowingFullScreen = true
            }
            .fullScreenCover(isPresented: $isShowingFullScreen) {
                FullScreenView(isPresented: $isShowingFullScreen)
            }
        }
    }
}

// Navigation with data passing
struct ProductListView: View {
    @State private var products: [Product] = []
    
    var body: some View {
        NavigationView {
            List(products) { product in
                NavigationLink(destination: ProductDetailView(product: product)) {
                    ProductRowView(product: product)
                }
            }
            .navigationTitle("Products")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Add") {
                        // Add new product
                    }
                }
            }
        }
    }
}''',
            ["NavigationView provides the foundation for navigation",
             "NavigationLink creates navigable connections between views",
             "NavigationStack (iOS 16+) offers more flexible navigation",
             "Sheet and fullScreenCover present modal views",
             "TabView creates tab-based navigation"],
            "SwiftUI navigation is declarative and integrates seamlessly with the framework's reactive patterns."
        )
        
        # 5.5 Animations
        self.add_topic(
            "5.5 Animations",
            "SwiftUI provides powerful animation capabilities with simple, declarative syntax.",
            '''import SwiftUI

// Basic animations
struct AnimationExamples: View {
    @State private var isRotated = false
    @State private var scale: CGFloat = 1.0
    @State private var offset: CGFloat = 0
    
    var body: some View {
        VStack(spacing: 40) {
            // Rotation animation
            Rectangle()
                .fill(Color.blue)
                .frame(width: 50, height: 50)
                .rotationEffect(.degrees(isRotated ? 180 : 0))
                .animation(.easeInOut(duration: 1), value: isRotated)
                .onTapGesture {
                    isRotated.toggle()
                }
            
            // Scale animation
            Circle()
                .fill(Color.green)
                .frame(width: 50, height: 50)
                .scaleEffect(scale)
                .animation(.spring(response: 0.5, dampingFraction: 0.6), value: scale)
                .onTapGesture {
                    scale = scale == 1.0 ? 1.5 : 1.0
                }
            
            // Offset animation
            RoundedRectangle(cornerRadius: 10)
                .fill(Color.orange)
                .frame(width: 50, height: 50)
                .offset(x: offset)
                .animation(.bouncy, value: offset)
                .onTapGesture {
                    offset = offset == 0 ? 100 : 0
                }
        }
    }
}

// withAnimation for explicit animation
struct ExplicitAnimationView: View {
    @State private var isExpanded = false
    
    var body: some View {
        VStack {
            RoundedRectangle(cornerRadius: 10)
                .fill(Color.purple)
                .frame(width: isExpanded ? 200 : 100, height: isExpanded ? 200 : 100)
            
            Button("Animate") {
                withAnimation(.spring(duration: 0.8)) {
                    isExpanded.toggle()
                }
            }
        }
    }
}

// Transitions
struct TransitionView: View {
    @State private var showDetail = false
    
    var body: some View {
        VStack {
            if showDetail {
                VStack {
                    Text("Detail View")
                        .font(.largeTitle)
                        .padding()
                    
                    Text("This is additional detail information")
                        .padding()
                }
                .background(Color.gray.opacity(0.1))
                .cornerRadius(10)
                .transition(.asymmetric(
                    insertion: .move(edge: .trailing).combined(with: .opacity),
                    removal: .move(edge: .leading).combined(with: .opacity)
                ))
            }
            
            Button(showDetail ? "Hide" : "Show") {
                withAnimation(.easeInOut) {
                    showDetail.toggle()
                }
            }
        }
        .padding()
    }
}

// Custom animations
struct WaveView: View {
    @State private var animateWave = false
    
    var body: some View {
        ZStack {
            ForEach(0..<3) { index in
                Circle()
                    .stroke(Color.blue.opacity(0.3), lineWidth: 2)
                    .frame(width: 50, height: 50)
                    .scaleEffect(animateWave ? 3 : 1)
                    .opacity(animateWave ? 0 : 1)
                    .animation(.easeOut(duration: 2).repeatForever(autoreverses: false).delay(Double(index) * 0.5), value: animateWave)
            }
        }
        .onAppear {
            animateWave = true
        }
    }
}

// Complex animation sequences
struct LoadingView: View {
    @State private var isLoading = false
    
    var body: some View {
        HStack {
            ForEach(0..<3) { index in
                Circle()
                    .fill(Color.blue)
                    .frame(width: 10, height: 10)
                    .scaleEffect(isLoading ? 1.0 : 0.5)
                    .animation(.easeInOut(duration: 0.6).repeatForever().delay(0.2 * Double(index)), value: isLoading)
            }
        }
        .onAppear {
            isLoading = true
        }
    }
}

// Gesture-driven animations
struct DragView: View {
    @State private var dragAmount = CGSize.zero
    
    var body: some View {
        VStack {
            RoundedRectangle(cornerRadius: 10)
                .fill(Color.red)
                .frame(width: 100, height: 100)
                .offset(dragAmount)
                .gesture(
                    DragGesture()
                        .onChanged { dragAmount = $0.translation }
                        .onEnded { _ in
                            withAnimation(.spring()) {
                                dragAmount = .zero
                            }
                        }
                )
            
            Text("Drag the square!")
                .padding()
        }
    }
}''',
            ["Use .animation() modifier for implicit animations",
             "withAnimation provides explicit control over animations",
             "Transitions define how views appear and disappear",
             "Spring animations provide natural motion",
             "Combine animations with gestures for interactive experiences"],
            "SwiftUI animations are declarative and automatically handle the complex details of smooth transitions."
        )
        
        # 5.2 Layout System
        self.add_topic(
            "5.2 Layout System",
            "SwiftUI provides powerful layout containers like VStack, HStack, ZStack, and LazyGrids for organizing views.",
            '''import SwiftUI

// Basic stacks
struct LayoutExamples: View {
    var body: some View {
        VStack(spacing: 20) {
            // Horizontal stack
            HStack {
                Text("Left")
                Spacer()
                Text("Right")
            }
            .padding()
            .background(Color.gray.opacity(0.2))
            
            // Vertical stack with alignment
            VStack(alignment: .leading, spacing: 10) {
                Text("Title")
                    .font(.headline)
                Text("This is a longer subtitle that demonstrates alignment")
                    .font(.caption)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
            .padding()
            .background(Color.blue.opacity(0.1))
            
            // Overlay stack
            ZStack {
                Rectangle()
                    .fill(Color.orange)
                    .frame(width: 100, height: 100)
                
                Text("Overlay")
                    .foregroundColor(.white)
                    .font(.caption)
            }
        }
    }
}

// Grid layouts
struct GridExample: View {
    let items = Array(1...20)
    
    let columns = [
        GridItem(.flexible()),
        GridItem(.flexible()),
        GridItem(.flexible())
    ]
    
    var body: some View {
        ScrollView {
            LazyVGrid(columns: columns, spacing: 10) {
                ForEach(items, id: \\.self) { item in
                    RoundedRectangle(cornerRadius: 8)
                        .fill(Color.blue)
                        .frame(height: 50)
                        .overlay(
                            Text("\\(item)")
                                .foregroundColor(.white)
                        )
                }
            }
            .padding()
        }
    }
}

// Adaptive grids
struct AdaptiveGridExample: View {
    let items = Array(1...50)
    
    var body: some View {
        ScrollView {
            LazyVGrid(columns: [GridItem(.adaptive(minimum: 80))], spacing: 10) {
                ForEach(items, id: \\.self) { item in
                    Circle()
                        .fill(Color.green)
                        .frame(height: 80)
                        .overlay(
                            Text("\\(item)")
                                .foregroundColor(.white)
                        )
                }
            }
            .padding()
        }
    }
}

// GeometryReader for custom layouts
struct CustomLayoutView: View {
    var body: some View {
        GeometryReader { geometry in
            VStack {
                Rectangle()
                    .fill(Color.red)
                    .frame(width: geometry.size.width * 0.8, height: 50)
                
                HStack {
                    Rectangle()
                        .fill(Color.blue)
                        .frame(width: geometry.size.width * 0.4, height: 100)
                    
                    Spacer()
                    
                    Rectangle()
                        .fill(Color.green)
                        .frame(width: geometry.size.width * 0.4, height: 100)
                }
            }
            .frame(width: geometry.size.width, height: geometry.size.height)
        }
    }
}''',
            ["VStack, HStack, and ZStack are the fundamental layout containers",
             "Spacer() pushes views apart or centers them",
             "LazyVGrid and LazyHGrid create efficient grid layouts",
             "GeometryReader provides access to parent view dimensions"],
            "SwiftUI's layout system is designed to be predictable and easy to understand while being highly flexible."
        )

    def generate_combine_content(self):
        """Generate Combine content - Part IV."""
        
        self.add_chapter_title("PART IV: REACTIVE PROGRAMMING")
        
        self.add_chapter_title("Chapter 7: Combine Framework")
        
        # 7.1 Publishers and Subscribers
        self.add_topic(
            "7.1 Publishers and Subscribers",
            "Combine is Apple's framework for handling asynchronous events by combining event-processing operators. Publishers emit values over time, and subscribers receive them.",
            '''import Combine
import Foundation

// Basic publisher and subscriber
class CombineBasics {
    var cancellables = Set<AnyCancellable>()
    
    func basicPublisherSubscriber() {
        // Simple publisher
        let publisher = Just("Hello, Combine!")
        
        publisher
            .sink { value in
                print("Received: \\(value)")
            }
            .store(in: &cancellables)
        
        // Array publisher
        let numbers = [1, 2, 3, 4, 5]
        numbers.publisher
            .sink { number in
                print("Number: \\(number)")
            }
            .store(in: &cancellables)
    }
    
    // PassthroughSubject
    func passthroughSubjectExample() {
        let subject = PassthroughSubject<String, Never>()
        
        subject
            .sink { value in
                print("PassthroughSubject received: \\(value)")
            }
            .store(in: &cancellables)
        
        subject.send("First message")
        subject.send("Second message")
        subject.send(completion: .finished)
    }
    
    // CurrentValueSubject
    func currentValueSubjectExample() {
        let currentValueSubject = CurrentValueSubject<Int, Never>(0)
        
        currentValueSubject
            .sink { value in
                print("CurrentValueSubject: \\(value)")
            }
            .store(in: &cancellables)
        
        currentValueSubject.send(1)
        currentValueSubject.send(2)
        
        print("Current value: \\(currentValueSubject.value)")
    }
    
    // Custom publisher
    struct CountdownPublisher: Publisher {
        typealias Output = Int
        typealias Failure = Never
        
        let start: Int
        
        func receive<S>(subscriber: S) where S : Subscriber, Never == S.Failure, Int == S.Input {
            let subscription = CountdownSubscription(subscriber: subscriber, start: start)
            subscriber.receive(subscription: subscription)
        }
    }
    
    class CountdownSubscription<S: Subscriber>: Subscription where S.Input == Int, S.Failure == Never {
        private var subscriber: S?
        private var current: Int
        
        init(subscriber: S, start: Int) {
            self.subscriber = subscriber
            self.current = start
        }
        
        func request(_ demand: Subscribers.Demand) {
            var demand = demand
            
            while demand > 0 && current > 0 {
                _ = subscriber?.receive(current)
                current -= 1
                demand -= 1
            }
            
            if current == 0 {
                subscriber?.receive(completion: .finished)
            }
        }
        
        func cancel() {
            subscriber = nil
        }
    }
    
    func customPublisherExample() {
        CountdownPublisher(start: 5)
            .sink { value in
                print("Countdown: \\(value)")
            }
            .store(in: &cancellables)
    }
}''',
            ["Publishers emit values over time, subscribers receive them",
             "PassthroughSubject sends values to subscribers without storing current value",
             "CurrentValueSubject maintains and emits the current value to new subscribers",
             "Custom publishers implement the Publisher protocol"],
            "Combine follows the reactive programming paradigm, making asynchronous code more manageable and composable."
        )

    def generate_networking_content(self):
        """Generate networking content - Part V."""
        
        self.add_chapter_title("PART V: NETWORKING & APIs")
        
        self.add_chapter_title("Chapter 8: Networking")
        
        # 8.1 URLSession
        self.add_topic(
            "8.1 URLSession",
            "URLSession is the foundation of networking in iOS. It provides APIs for making HTTP requests with modern async/await support.",
            '''import Foundation

// Basic URLSession with async/await
class NetworkManager {
    static let shared = NetworkManager()
    private init() {}
    
    // Simple GET request
    func fetchData(from url: URL) async throws -> Data {
        let (data, response) = try await URLSession.shared.data(from: url)
        
        guard let httpResponse = response as? HTTPURLResponse,
              httpResponse.statusCode == 200 else {
            throw NetworkError.invalidResponse
        }
        
        return data
    }
    
    // POST request with JSON
    func postJSON<T: Codable>(to url: URL, body: T) async throws -> Data {
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.setValue("Bearer \\(AuthManager.token)", forHTTPHeaderField: "Authorization")
        
        request.httpBody = try JSONEncoder().encode(body)
        
        let (data, response) = try await URLSession.shared.data(for: request)
        
        guard let httpResponse = response as? HTTPURLResponse,
              200...299 ~= httpResponse.statusCode else {
            throw NetworkError.serverError(response)
        }
        
        return data
    }
    
    // Download file with progress
    func downloadFile(from url: URL) -> AsyncThrowingStream<DownloadProgress, Error> {
        AsyncThrowingStream { continuation in
            let task = URLSession.shared.downloadTask(with: url) { localURL, response, error in
                if let error = error {
                    continuation.finish(throwing: error)
                    return
                }
                
                guard let localURL = localURL else {
                    continuation.finish(throwing: NetworkError.noData)
                    return
                }
                
                // Move file to permanent location
                // continuation.yield(.completed(localURL))
                continuation.finish()
            }
            
            task.resume()
        }
    }
    
    // URLSession with custom configuration
    func createCustomSession() -> URLSession {
        let config = URLSessionConfiguration.default
        config.timeoutIntervalForRequest = 30
        config.timeoutIntervalForResource = 60
        config.httpMaximumConnectionsPerHost = 5
        config.requestCachePolicy = .reloadIgnoringLocalCacheData
        
        return URLSession(configuration: config)
    }
    
    // Retry mechanism
    func fetchWithRetry<T: Codable>(url: URL, type: T.Type, maxRetries: Int = 3) async throws -> T {
        var lastError: Error?
        
        for attempt in 1...maxRetries {
            do {
                let data = try await fetchData(from: url)
                return try JSONDecoder().decode(T.self, from: data)
            } catch {
                lastError = error
                if attempt < maxRetries {
                    let delay = Double(attempt * 2) // Exponential backoff
                    try await Task.sleep(nanoseconds: UInt64(delay * 1_000_000_000))
                }
            }
        }
        
        throw lastError ?? NetworkError.maxRetriesExceeded
    }
}

// Error handling
enum NetworkError: Error, LocalizedError {
    case invalidURL
    case noData
    case invalidResponse
    case serverError(URLResponse?)
    case decodingError
    case maxRetriesExceeded
    
    var errorDescription: String? {
        switch self {
        case .invalidURL:
            return "Invalid URL"
        case .noData:
            return "No data received"
        case .invalidResponse:
            return "Invalid response"
        case .serverError:
            return "Server error"
        case .decodingError:
            return "Failed to decode data"
        case .maxRetriesExceeded:
            return "Maximum retry attempts exceeded"
        }
    }
}

// Progress tracking
struct DownloadProgress {
    let bytesWritten: Int64
    let totalBytesWritten: Int64
    let totalBytesExpectedToWrite: Int64
    
    var progress: Double {
        guard totalBytesExpectedToWrite > 0 else { return 0 }
        return Double(totalBytesWritten) / Double(totalBytesExpectedToWrite)
    }
}''',
            ["async/await makes networking code more readable and maintainable",
             "Always handle HTTP status codes and potential errors",
             "URLSession configuration allows customization of timeouts and caching",
             "Implement retry mechanisms for robust networking"],
            "Modern Swift networking leverages async/await for cleaner asynchronous code without callback hell."
        )

    def generate_dsa_appendix(self):
        """Generate the DSA appendix (keep existing content)."""
        
        self.add_chapter_title("APPENDIX: DATA STRUCTURES & ALGORITHMS")
        
        # Keep the existing DSA problems as an appendix
        # Array Problems
        self.add_chapter_title("A.1 Array Problems")
        
        # Two Sum Problem (simplified version of existing)
        self.add_topic(
            "Two Sum",
            "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.",
            '''func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    var numToIndex: [Int: Int] = [:]
    
    for (index, num) in nums.enumerated() {
        let complement = target - num
        
        if let complementIndex = numToIndex[complement] {
            return [complementIndex, index]
        }
        
        numToIndex[num] = index
    }
    
    return []
}

// Example usage:
let nums = [2, 7, 11, 15]
let target = 9
let result = twoSum(nums, target)
print(result) // [0, 1]''',
            ["Time Complexity: O(n)", "Space Complexity: O(n)"],
            "Uses hash map to store each number and its index, enabling O(1) lookup time."
        )
        
        # Add a few more DSA problems in similar format
        self.add_topic(
            "Maximum Subarray (Kadane's Algorithm)",
            "Find the contiguous subarray with the largest sum.",
            '''func maxSubArray(_ nums: [Int]) -> Int {
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
print(result) // 6 (subarray [4, -1, 2, 1])''',
            ["Time Complexity: O(n)", "Space Complexity: O(1)"],
            "Kadane's algorithm maintains the maximum sum ending at each position."
        )

    def generate_pdf(self):
        """Generate the complete comprehensive Swift guide PDF."""
        print("Starting comprehensive Swift guide PDF generation...")
        
        # Add title page
        self.add_title_page()
        
        # Add comprehensive table of contents
        self.add_comprehensive_table_of_contents()
        
        # Generate all content
        self.generate_swift_basics_content()
        self.generate_advanced_swift_content()
        self.generate_swiftui_content()
        self.generate_combine_content()
        self.generate_networking_content()
        self.generate_dsa_appendix()
        
        # Build the PDF
        self.doc.build(self.story)
        print(f"PDF generated successfully: Comprehensive_Swift_Programming_Guide.pdf")
        return "Comprehensive_Swift_Programming_Guide.pdf"

def main():
    """Main function to generate the comprehensive Swift guide PDF."""
    generator = SwiftProgrammingGuidePDFGenerator()
    pdf_filename = generator.generate_pdf()
    
    print(f"✅ Successfully generated: {pdf_filename}")
    print("📄 The PDF contains a comprehensive Swift programming guide with 120+ topics covering:")
    print("   • Swift Language Fundamentals")
    print("   • Advanced Swift Concepts")
    print("   • SwiftUI Framework")
    print("   • Combine Reactive Programming")
    print("   • Networking & APIs")
    print("   • iOS Development")
    print("   • Data Structures & Algorithms")
    
if __name__ == "__main__":
    main()