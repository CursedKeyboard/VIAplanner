const express = require("express")
const Course = require("../models/course")
const router = new express.Router()

// route to get all course data for the search bar
router.get("/courses/searchbar", async (req, res) => {
    try {

        const allCourses = await Course.find({})
        let allSearchBarValues = []
        for (let course of allCourses) {
            allSearchBarValues.push({ courseCode: course.courseCode, name: course.name })
        }

        res.send(allSearchBarValues)

    } catch (e) {
        res.status(500).send({ message: e.message })
    }
})

// route for getting data about a specific course
router.get("/courses/:courseCode", async (req, res) => {

    try {

        const course = await Course.findOne({ courseCode: req.params.courseCode })

        if (!course) {
            res.status(404).send({ message: "no course exist with this code" })
        }
        else {
            res.send(course)
        }

    } catch (e) {
        res.status(500).send({ message: e.message })
    }

})

// route to get all courses
router.get("/courses", async (req, res) => {

    try {
        const allCourses = await Course.find({})
        res.send(allCourses)
    } catch (e) {
        res.status(500).send({ message: e.message })
    }

})

// route for create a course
router.post("/courses", async (req, res) => {

    try {
        const currCourse = new Course(req.body)

        await currCourse.save()
        res.status(201).send({ message: "course created successfully" })
    } catch (e) {
        res.status(500).send({ message: e.message })
    }

})

module.exports = router