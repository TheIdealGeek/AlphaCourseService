"""
Class Definition of Course API
@author meShakti 29-04-2015 7:55 AM
"""

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = 'org.alpha.CourseService'

#region to represent task definition
class QuizData(messages.Message):
    #Quiz data definition
    #TODO find what this 1 in parameter does
    optionA = messages.StringField(1)
    optionB = messages.StringField(2)
    optionC = messages.StringField(3) 
    optionD = messages.StringField(4)   
    question = messages.StringField(5)
    answer = messages.StringField(6)

class Task(messages.Message):
    #Task class definition
    taskId = messages.StringField(1)
    taskTitle = messages.StringField(2)
    taskDesc = messages.StringField(3)
    taskType =messages.StringField(4)
    quizData = messages.MessageField(QuizData,5,repeated=True)

#region to represent Module
class Module(messages.Message):
    #Module class definition
    moduleId = messages.StringField(1)
    moduleTitle = messages.StringField(2)
    moduleDesc = messages.StringField(3)
    taskId =messages.StringField(4,repeated=True) #Possible error area
    
#region to represent Course
class Course(messages.Message):
    #Course class definition
    courseId = messages.StringField(1)
    moduleList = messages.StringField(2,repeated=True)
    taskList = messages.StringField(3,repeated=True)

#region to represent Course Info and list

class CourseInfo(messages.Message):
    #CourseInfo class definition
    courseId = messages.StringField(1)
    courseTitle = messages.StringField(2)
    courseDesc = messages.StringField(3)
 
class CourseList(messages.Message):
    #CourseList class definition
    courseInfo = messages.MessageField(CourseInfo,1,repeated=True)