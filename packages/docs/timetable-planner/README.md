---
sidebar: auto
---
# Timetable Planner

A web app that helps UofT students plan their courses to generate their optimal timetable. 

The timetable planner allows students to enter their course load and get back a timetable that fits their needs. The vision for the timetable planner includes taking student preferences into account such as: 

- How early students wish to start and end classes
- What days students would like to take off
- What times students would prefer gap time and breaks


## Overview

![timetable-journey](./Timetable-journey.png)

Once the user selects the courses from the Course Guide:

![coursechosing](./coursechosing.png)

The user views the timetable:

The timetable will display whether or not if the selected courses have a valid time, that is no conflict for all courses.

 - Valid:
 
![timetable](./timetable.png)

 - Invalid:
 
![error1](./error1.png)

There are serveral preferences that the user can select to optimize the timetable:

![timetableconstraint](./timetableconstraint.png)


 - Minimize/Maximize idle time: The user can maximize or minimize the gap time between courses.
 - Days off: The user can select the day(s) off so there will be no course appear on that day.
 - Avoid Morning/Evening Class: The user can choose whether if they want to have courses in the morning or evening.
 
The timetable will return invalid and displays a message if the constraints are unreachable.

![error2](./error2.png)

The user can also choose to lock certain course times. 

When preferences are made, those times will not be changed.

![lock1](./lock1.png)

after a course is locked and a preference is being made:

![lock2](./lock2.png)

## Roadmap for the Timetable Algorithm
<!---
- Introduce what the timetable algorithm is for
- Tell a story about how the algorithm evolves
- Have a heading for each optimization in the roadmap
- Start with base conflict check -> invalid times -> idle time max/min -> locked courses
--->
The timetable algorithm takes in a set of course names and outputs a list of timetables. The user can optimize the timetable to fit their preference.

The algorithm are separated into 3 main components: 

The first component makes the combinations of sections of each course and the combinations of the above combinations of all the courses. 

The next component creates the timetable from the combination of the courses and make a collection of all the possible timetables.

The last component is the constraints towards the timetables.They work as a filter towards the collection of all timetables. 

### Combination Component

This component creates combinations of sections of each course and the combinations of the above combinations of all the courses. 


**Pseudocode**
```js
/**
 *
 * Creates the combination of section in a course
 * @param {Course} course
 * @returns {CourseMeetingSectionCombinations}
 */
const courseMeetingSectionCombinations = (course: Course): CourseMeetingSectionCombinations => {
    combination = []
    for (lecture of course.meeting_sections){
        combination.push(lecture)
    }
    for (exist_section of combination){
        for (tutorial of course.meeting_sections){
            exist_section.push(tutorial)
        }
        for (practice of course.meeting_sections){
            exist_section.push(practice)
        }
    }
    return combination
}

/**
 *
 * Creates the combination of courses of their section combinations
 * @param {CourseMeetingSectionCombinations[]} courseMeetingSectionCombos
 * @returns {MeetingSection[][]}
 */
const courseCombinations = (courseMeetingSectionCombos: CourseMeetingSectionCombinations[]): MeetingSection[][] => {
    output = []
    Recursively search for the next course section combination and append each combination to the output until the last course.
    return output
}
```

### Timetable Component

This component serves as the main function to generate all possible timetables from the combinations.

**Pseudocode**
```js
/**
 *
 * Checks overlap of course times for each day in a timetable
 * @param {Timetable} timetable
 * @returns {boolean}
 */
const overlapExists = (timetable: Timetable): boolean => {
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
    for (day of days){
        for (section of timetable[day]){
            section2 = section + 1
            for (section2 smaller then timetable[day].length){
                if (section overlap with section2){
                    return true
                }
            }
        }
    }
    return false
}


/**
 *
 * Creates timetable by parse the meetingSections into each day and check for validity
 * @param {MeetingSection[]} meetingSectionCombo
 * @returns {Timetable}
 */
const createTimetable = (meetingSectionCombo: MeetingSection[]): Timetable => {
    timetable = {}
    for (section of meetingSectionCombo){
        for (time of section){
            timetable[time.day].push(time)
        }
    }
    if (not overlapExists(timetable)){
        return timetable
    }
}


/**
 *
 * The main function.
 * Starts from produce all section combinations of each course
 * Produce the combinations of the courses' section combinations
 * Create Timetable for each combinations of section combinations
 * Returns the master list of Timetables
 * @param {Course[]} courses
 * @returns {Timetable[]}
 */
const generateTimetables = (courses: Course[]): Timetable[] => {
    meetingSectionCombos = []
    for (course of courses){
    meetingSectionCombos.push(courseMeetingSectionCombinations(course))
    }
    courseCombo = courseCombinations(meetingSectionCombos)
    timetables = []
    for (combination of courseCombo){
        timetables.push(createTimetable(combination))
    }
    return timetables

}
```
### Constraint Component

This component is the constraint for the timetable.
It acts like a filter towards the collection of the possible timetable.

**Pseudocode**

```js
/**
 *
 * Append timeOffs sections to each timetable and check for their validity again
 * @param {Timetable[]} timetables
 * @param {Timetable} timeOffs
 * @returns {Timetable[]}
 */
const timeOffs = (timetables: Timetable[], timeOffs: Timetable): Timetable[] => {
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
    for (day of days){
        timetables[day].push(timeOffs[day])
    }
    if (not overlapExists(timetable)){
        return timetable
    }
}

/**
 *
 * Based on the option returns the max or min idle time at school timetable from the timetables  
 * @param {Timetable[]} timetables
 * @param {string} option
 * @returns {Timetable}
 */
const idleTime = (timetables: Timetable[], option: string): Timetable => {
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY']
    sums = []
    for (timetable of timetables){
        sum = 0
        for (day of days){
            for (section of timetables[day]){
                section2 = section + 1
                for (section2 smaller then timetables[day].length){
                    sum += section.end - section2.start
                }
            }
        }
        sums.push(sum)
    }
    return timetable[indexOf(sums.option)]
}
```

