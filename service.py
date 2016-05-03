"""
Course API  implemented using Google Cloud Endpoints.

Defined here are ProtoRPC messages needed to define Schemas for methods as well as
those methods defined in an API.

@author meShakti 29-04-2015 7:50 AM
"""


from dummyData import *

@endpoints.api(name='courseService', version='v1')
class CourseApi(remote.Service):
  """Course Dummy  API v1."""
  COURSE_RESOURCE= endpoints.ResourceContainer(
    courseId = messages.StringField(1,required=True)
    )
  """ Method to get course by id"""
  @endpoints.method(COURSE_RESOURCE,Course,
                  path='course/{courseId}', http_method='POST',
                  name='course.getCourseById')
  def getCourseById (self, request):
    if(request.courseId == 'DB101'):
         return COURSES[0]
    else:
        return Course()
  
  """ Method to get module by id"""
  MODULE_RESOURCE= endpoints.ResourceContainer(
    moduleId = messages.StringField(1,required=True)
    )
  @endpoints.method(MODULE_RESOURCE, Module,
                    path='module/{moduleId}', http_method='POST',
                    name='course.getModuleById')
  def getModuleById(self,request):
    if(request.moduleId == 'DBMOD101'):
      return MODULE_LIST[0]
    else:
      return Module()
      
  """ Method to get Task by id"""
  TASK_RESOURCE= endpoints.ResourceContainer(
    taskId = messages.StringField(1,required=True)
    )
  @endpoints.method(TASK_RESOURCE, Task,
                    path='task/{taskId}', http_method='POST',
                    name='course.getTaskById')
  def getTaskById(self,request):
    if(request.taskId == 'TSK101'):
      return TASK_LIST[0]
    elif(request.taskId == 'TSK102'):
      return TASK_LIST[1]
    elif(request.taskId == 'TSK103'):
      return TASK_LIST[2]
    else:
      return Task()
      
  """ Method to get yo CourseList by beginining index and length"""
  COURSE_LIST_RESOURCE= endpoints.ResourceContainer(
    beginIndex = messages.IntegerField(1),count = messages.IntegerField(2)
    )
  @endpoints.method(COURSE_LIST_RESOURCE, CourseList,
                    path='courselist/{beginIndex}/{count}', http_method='POST',
                    name='course.getAllCourseList')
  def getAllCourseList(self,request):
        beginIndex = request.beginIndex
        count = request.count
        course_info = COURSE_LIST.courseInfo
        if beginIndex is None:
            return COURSE_LIST
        if count is None :
            if beginIndex < len(course_info):
                    return CourseList(courseInfo=course_info[beginIndex:])
        if (count+beginIndex-1 <len(course_info)):
            return CourseList(courseInfo=course_info[beginIndex:count])
        return CourseList()
"""
  ID_RESOURCE = endpoints.ResourceContainer(
      message_types.VoidMessage,
      id=messages.IntegerField(1, variant=messages.Variant.INT32))

  @endpoints.method(ID_RESOURCE, Greeting,
                    path='hellogreeting/{id}', http_method='GET',
                    name='greetings.getGreeting')
  def greeting_get(self, request):
    try:
      return STORED_GREETINGS.items[request.id]
    except (IndexError, TypeError):
      raise endpoints.NotFoundException('Greeting %s not found.' %
                                        (request.id,))
"""
APPLICATION = endpoints.api_server([CourseApi])


    
    
    
    
    
    