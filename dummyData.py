"""
Dummy Data for the Service
"""

from serviceClass import *

#Array for storing course Info
COURSE_LIST = CourseList(
    courseInfo=[
        CourseInfo(
            courseId ="DB101",
            courseTitle="Data Structure",
            courseDesc ="Course Describing Data Structue and giving brief overview of main data structures like stack , queues etcyo"
        )
    ]
)

#Sample data for quiz
QUIZ_DATA = [
    QuizData(
      optionA ="logN",
      optionB ="N^2",
      optionC ="N",
      optionD="e^N",
      question ="what is the average complexity of bubble sort with early exit?",
      answer ="optionB"  
    ),
    QuizData(
      optionA ="N",
      optionB ="N^2",
      optionC ="e^N",
      optionD="Constant",
      question ="what is the space complexity of Merge Sort?",
      answer ="optionA"  
    ),
    QuizData(
      optionA ="N",
      optionB ="N^3",
      optionC ="e^N",
      optionD="Constant",
      question ="what is the space complexity of Quick Sort?",
      answer ="optionD"  
    ),
    QuizData(
      optionA ="logN",
      optionB ="N",
      optionC ="Constant",
      optionD="N^2",
      question ="what is average time complexity of binary search?",
      answer ="optionA"  
    ),
    QuizData(
      optionA ="First Element",
      optionB ="Last Element",
      optionC ="Random Element",
      optionD="It comes from hash function",
      question ="What will be the good choice of pivot in Quick sort?",
      answer ="optionC"  
    ),
]
#contains lists of tasks
TASK_LIST = [
    Task(
       taskId ="TSK101",
       taskTitle="Quick Sort Overview",
       taskDesc ="Sample Description To describe Quick sort",
       taskType ="THEORY",
       quizData =[] 
    ),
      Task(
       taskId ="TSK102",
       taskTitle="Print Hello in python",
       taskDesc ="print 'Hello World' ",
       taskType ="PROGRAM",
       quizData =[] 
    ),
      Task(
       taskId ="TSK103",
       taskTitle="Complexity Quiz",
       taskDesc ="Some Quiz questions on Time and Quiz complexity",
       taskType ="Quiz",
       quizData =QUIZ_DATA 
    )
]

#For module sample data
MODULE_LIST = [
    Module(
       moduleId ="DBMOD101",
       moduleTitle = "Analysis of Algorithim",
       moduleDesc = "Contains Description on how to measure performance of algorithim",
       taskId =["TSK101","TSK102","TSK103"] 
    )
]

#For Course sample data
COURSES =[
    Course(
        courseId ="DB101",
        moduleList =["DBMOD101"],
        taskList = ["TSK101","TSK102","TSK103"]
    )
]
