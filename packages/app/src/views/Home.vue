<template>
    <v-row>
        <v-col class="ma-0 pt-0 pb-0">
            <!-- Popup tutorial -->
            <tutorial />
            <!--Exporting Progress Overlay-->
            <v-overlay :value="getExportOverlay">
                <v-row>
                    <h1 class="ma-3">Exporting</h1>
                </v-row>
                <v-row justify="center">
                    <v-progress-circular
                        indeterminate
                        size="64"
                        style="margin-left: auto ; margin-right: auto ;"
                    ></v-progress-circular>
                </v-row>
            </v-overlay>

            <v-toolbar dark color="#012B5C" height="58px" elevation="0">
                <v-img
                    src="../assets/VIA-Planner-White.png"
                    max-width="130"
                    contain
                    class="ma-2 ml-1"
                />
                <v-tabs grow v-model="whichTab" style="max-width: 250px; min-width: 250px">
                    <v-tab>PROGRAMS</v-tab>
                    <v-tab>TIMETABLE</v-tab>
                </v-tabs>
                <course-search-bar style="margin: auto" />
                <switch-sem style="margin: auto" />
            </v-toolbar>
            <v-row>
                <v-col class="pa-0">
                    <router-view />
                    <v-footer class="white">
                        <v-row>
                            <v-col class="pa-0">
                                <h1
                                    style="text-align:center"
                                    class="text-subtitle-1"
                                >
                                    Copyright © 2020 VIAplanner - Data updated for
                                    the 2020 - 2021 school year
                                </h1>
                            </v-col>
                        </v-row>
                    </v-footer>
                </v-col>
                <v-col cols="3" class="grey lighten-4 mr-2">
                    <side-bar />
                </v-col>
            </v-row>
        </v-col>
    </v-row>
</template>

<script>
import CourseSearchBar from "../components/AppBar/CourseSearchBar";
import Tutorial from "../components/Popup/Tutorial";
import SwitchSem from "../components/AppBar/SwitchSem";
import SideBar from "../components/SidePanel/SideBar";
import { mapGetters } from "vuex";

export default {
    created() {
        if (this.$isMobile()) {
            this.$router.push({ name: "about" });
        } else {
            window.addEventListener("beforeunload", this.saveData);
        }
    },
    components: {
        SwitchSem,
        CourseSearchBar,
        Tutorial,
        SideBar,
    },
    computed: {
        ...mapGetters([
            "getSemesterStatus",
            "getExportOverlay",
            "fallTimetable",
            "winterTimetable",
            "fallSelectedCourses",
            "winterSelectedCourses",
            "fallLockedSections",
            "winterLockedSections",
        ]),
    },
    methods: {
        // save the timetable data in the browser
        saveData() {
            localStorage.fallLockedSections =  JSON.stringify(this.fallLockedSections)
            localStorage.fallSelectedCourses = JSON.stringify(this.fallSelectedCourses)
            localStorage.fallTimetable = JSON.stringify(this.fallTimetable)
            localStorage.winterLockedSections = JSON.stringify(this.winterLockedSections)
            localStorage.winterSelectedCourses = JSON.stringify(this.winterSelectedCourses)
            localStorage.winterTimetable = JSON.stringify(this.winterTimetable)
        },
    },
    data() {
        return {
            scrollBarSettings: {
                wheelPropagation: false,
                maxScrollbarLength: 240,
                swipeEasing: true,
                wheelSpeed: 0.1,
            },
            whichTab: 1,
        };
    },
    watch: {
        whichTab() {
            if (this.whichTab === 0) {
                this.$router.push({ name: "program" });
            } else if (this.whichTab === 1) {
                this.$router.push({ name: "timetable" });
            }
        },
    },
};
</script>
<style scoped>
.timetableColumn {
    padding-top: 0px;
    height: 100%;
}
</style>
