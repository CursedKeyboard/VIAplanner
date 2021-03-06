<template>
    <div>
        <v-card :height="coursePanelHeight" class="pa-4">
            <h1 class="text-h6">{{ sideBarTitle }}</h1>
            <hr class="mb-1" />
            <v-row
                justify="center"
                align="center"
                :style="`height: ${coursePanelHeight * 0.85}px`"
                style="z-index: -1"
            >
                <img :src="imgSrc" style="position: absolute" :width="imgWidth" />
                <smooth-scrollbar class="right-scroll-area">
                    <v-expansion-panels
                        :v-model="whichCoursesExpanded"
                        multiple
                        hover
                        class="expansion-panel-settings pa-1"
                    >
                        <selected-course-card
                            v-for="(course, code) in filterCourses"
                            :key="code"
                            :course="course"
                        />
                    </v-expansion-panels>
                </smooth-scrollbar>
            </v-row>
        </v-card>
        <v-card :height="programPanelHeight" class="mt-3 pa-4">
            <v-overlay absolute opacity="0.3" z-index="1">
                <h1>Coming Soon</h1>
            </v-overlay>
            <h1 class="text-h6">Programs</h1>
            <hr class="mb-3" />
            <v-skeleton-loader type="list-item-avatar" />
            <v-skeleton-loader type="list-item-avatar-two-line" />
            <v-skeleton-loader v-if="programPanelHeight > 195" type="list-item-avatar" />
        </v-card>
    </div>
</template>
<script>
import SelectedCourseCard from "./SelectedCourseCard";
import { mapGetters } from "vuex";

export default {
    components: {
        SelectedCourseCard,
    },
    data() {
        return {
            whichCoursesExpanded: [],
        };
    },
    computed: {
        ...mapGetters(["selectedCourses", "getSemesterStatus", "timetable"]),
        sideBarTitle() {
            if (this.getSemesterStatus === "F") {
                return "Fall Courses";
            } else {
                return "Winter Courses";
            }
        },
        coursePanelHeight() {
            return (window.innerHeight - 99) * 0.6;
        },
        programPanelHeight() {
            return (window.innerHeight - 99) * 0.4;
        },
        imgWidth() {
            return window.innerWidth * 0.17;
        },
        imgSrc() {
            if (this.getSemesterStatus === "F") {
                return require("../../assets/fall-background.png");
            } else {
                return require("../../assets/winter-background.png");
            }
        },
        filterCourses() {
            this.timetable; //force re-render the selected courses
            const filteredCourses = {};

            for (var code in this.selectedCourses) {
                if (!code.includes("Lock")) {
                    filteredCourses[code] = this.selectedCourses[code];
                }
            }

            return filteredCourses;
        },
    },
};
</script>
<style scoped>
.right-scroll-area {
    position: relative;
    height: 90% !important;
    background-color: transparent;
    padding-left: 10px;
    padding-right: 10px;
}
.expansion-panels-settings {
    width: 90%;
}
</style>
