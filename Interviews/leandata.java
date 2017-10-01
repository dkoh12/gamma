
/**
 *
 * 
 * Know that you can have a table like
 *
 *
 * Courses
 * CID NAME
 *
 * Students
 * SID, NAME, CID
 *  1,  jon,  1
 *  1,  jon,  2
 *
 * Professors
 * PID NAME CID
 *
 *
 *
 * map SID to Name
 * SID | Name
 *
 * ****
 * You can combine SID and CID to be a separate table
 * When you have 2 foreign keys in hashtable that's ok, no primary keys
 * 
 * SID | CID
 *  1     1
 *  1     2
 *
 *
 * Combine everything to 
 * CID isProfessor(boolean) Name, Address, etc
 *
 * 
 */


/*

    Remember that you can map an Instance / Object into the hashtable.

    H[ID] = new Student()

    Then update the Student's variables accordingly

 */


/*

    Given a list of pairs

    A-B
    B-C
    C-D
    E-F

    [[A, B, C, D], [E, F]]

    Write code that can join them into sets
    
    ALSO Need to handle MERGES!!

    Time is O(n) or O(n log n). merge doesn't make it linear but it is usually linear.

    arr =[]
    d={}
    index = 0
    for i in lst:
        first, second = i
        if first not in d and second not in d:
            index += 1
            d[first] = index
            d[second] = index
            arr.append([first, second])
        elif first in d and second in d:
            a = d[first]
            b = d[second]
            while len(arr[b]) > 0:
                p = arr[b].pop()
                arr[a].append(p)   // erase not delete
        elif first not in d:
            curr = d[second]
            d[first] = curr
            arr[curr].append(first)
        else:
            curr = d[first]
            d[second] = curr
            arr[curr].append(second)



    let M = [[1, 2, 3],
            [10, 20],
            [5, 50, 500, 5000]]

    M is dynamic in size. We want to pick a value in each subarray and compute some machine learning algorithm.
    Imagine each subarray is a selection of values we can choose for that feature.

    for i in M[0]:
        for j in M[1]:
            for k in M[2]:
                run algo

    but you don't know how many forloops you need.

    What you can do instead is have an array of subarray sizes
    [3, 2, 4]
    3 * 2 * 4 = 24

    then...

    lst = [3, 2, 4]
    arr = [0, 0, 0]

    //counting problem
    [0,0,1], [0,0,2] .. [0,1,0]...

    index = len(arr)-1
    for i in range(24):
        if arr[index] + 1 = lst[index]:
            arr[index] = 0
            index -= 1



 */



Given the following utility methods that return arrays, write a function that will populate some fields on the Student object. A student can belong to multiple Courses & Clubs.

public class Student{
    String Id;
    String name;
    Integer numberOfCourses;
    Integer numberOfClubs;
    
    
    Integer TotalClassDuration;
    Integer TotalCredits;
    Integer CreditsFromHistory;
}

public class Course{
    String Id;
    String name;
    String department;
    Integer durationInMinutes;
    Integer numberOfCredits;
}

public class Club{
    String Id;
    String name;
    Integer numberOfCredits;
}

public class StudentCourseRelationship{
    String studentId;
    String courseId;
}

public class StudentClubRelationship{
    String studentId;
    String clubId;
}

Here are the utility methods you have access to :

public List<Student> getStudents() { } //Returns a List of Student objects from the database

public List<Course> getCourses()) { } //Returns a List of Course objects from the database

public List<Club> getClubs() { } //Returns a List of Club objects from the database

public List<StudentCourseRelationship> getStudentCourseRelationships() { } //Returns a List of StudentCourseRelationship objects from the database

public List<StudentClubRelationship> getStudentClubRelationships() { } //Returns a List of StudentClubRelationship objects from the database

public void saveToDatabase( List<Student> savedObjs ) {} // Saves a list of Objects to the database 

//1) Write a function that will populate NumberOfCourses & NumberOfClubs on the Student objects. 
/*
2) Add the following fields : 
        Add a new field 'TotalClassDuration' on the Student object and calculate that in your method. This is a sum of 'durationInMinutes' from Courses. 
*/

public void populateData(){
    Map<String,Student> studentsMap = new Map<String,Student>();
    Map<String,Course> coursesMap = new Map<String,Course>();
    Map<String,Club> clubsMap = new Map<String,Club>();

    for( Student s : getStudents() ){
        s.NumberOfClubs = 0;
        s.NumberOfCourses = 0;
        s.TotalClassDuration = 0;
        s.TotalCredits = 0;
        s.TotalCreditsFromHistory = 0;
        studentsMap.put( s.Id, s );
    }

    for( Course c : getCourses() )
        coursesMap.put( c.Id, c );
    
    for( Club cl : getClubs() )
        clubsMap.put( cl.Id, cl );

    for( StudentCourseRelationship scr : getStudentCourseRelationships() ){
        studentsMap.get( scr.studentId ).numberOfCourses++;
        studentsMap.get( scr.studentId ).TotalClassDuration += coursesMap.get(scr.courseId).durationInMinutes;
        studentsMap.get( scr.studentId ).TotalCredits += coursesMap.get(scr.courseId).numberOfCredits;

        if( coursesMap.get(scr.courseId).department == 'History' )
            studentsMap.get( scr.studentId ).CreditsFromHistory += coursesMap.get(scr.courseId).numberOfCredits;
    }

    for( StudentClubRelationship sclr : getStudentClubRelationships() ){
        studentsMap.get( sclr.studentId ).numberOfClubs++;
        studentsMap.get( sclr.studentId ).TotalCredits += clubsMap.get(sclr.clubId).numberOfCredits;
    }
    
    saveToDatabase( studentsMap.values() ); 
}



public void Populate() {
    List<Student> student = getStudents();
    List<Course> course = getCourses();
    List<Club> club = getClubs();
    List<StudentCourseRelationship> StudentCourse = getStudentCourseRelationship();
    List<StudentClubRelationship> StudentClub = getStudentClubRelationship();
    
    Hashtable<String, Integer> clubTable = new Hashtable<>();
    Hashtable<String, Integer> courseTable = new Hashtable<>();
    
    for(StudentCourseRelationship SCR : StudentCourse) {
        if(courseTable.contains(SCR.studentId)) {
            Integer i = courseTable.get(SCR.studentId);
            courseTable.get(SCR.studentId).replace(i+1);
        }
        else {
            courseTable.get(SCR.studentId).add(1);
        }
    
    }
    
    for(StudentClubRelationship SCR : StudentClub) {
        if(clubTable.contains(SCR.studentId)) {
            Integer i = clubTable.get(SCR.studentId);
            clubTable.get(SCR.studentId).replace(i+1);
        }
        else {
            clubTable.get(SCR.studentId).add(1);
        }
    }
    
    
    for(Student s : student) {
        s.NumberOfCourses = 0;
        
        if(courseTable.contains(s.Id)) {
            s.NumberOfCourses += courseTable.get(s.Id);
        }
        
        if(clubTable.contains(s.Id)) {
            s.NumberOfClubs += clubTable.get(s.Id);
        }
        
    }
    
    saveToDatabase(student);

}


















