# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
![Use case](https://github.com/DomTaoMeaw/unknownapp/blob/4a45854efc6c994bdb47703616a8232c7bd4c09c/image/Week11.drawio.png)
### Flowchart of the main workflow

```mermaid
flowchart TD
    A[Launch Application] --> B{Choose User Role}
    
    B -->|Student| C[Input Student ID or type 'new']
    C --> D{Is ID found?}
    D -->|Yes| E[Student Dashboard]
    D -->|No| F[Create New Student Record] --> E

    E --> E1[Browse Available Courses]
    E --> E2[Enroll in Course]
    E --> E3[Withdraw from Course]
    E --> E4[Check Personal Schedule]
    E --> E5[View Payment Details]
    E --> E6[Update Personal Information]
    E --> E7[Sign Out and Save]
    E7 --> G[Return to Main Screen]

    B -->|Admin| H[Enter Administrator Password]
    H --> I{Is Password Valid?}
    I -->|Yes| J[Administrator Panel]
    I -->|No| G

    J --> J1[Browse Course List]
    J --> J2[View Course Participants]
    J --> J3[List All Students]
    J --> J4[Create Student Record]
    J --> J5[Modify Student Information]
    J --> J6[Create New Course]
    J --> J7[Modify Course Details]
    J --> J8[View Student Timetable]
    J --> J9[Check Student Billing Info]
    J --> J10[Sign Out and Save]
    J10 --> G

    G -->|Continue Using System| B
    G -->|Terminate Program| K[Close Application]
```

### Prompts
"I selected the use case "Create New Student Profile", so your task is to create an equivalent Python version that allows users to input student ID, name, and major, store the data, and prevent duplicate IDs."
