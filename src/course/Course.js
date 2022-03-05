import Split from "react-split";
import "./Course.css";
import ChapterContext from "./ChapterContext.js";
import { useState } from "react";
import chapters from "./chapters";
import "typeface-anonymous-pro";

function Course() {
  const [curChapter, setCurChapter] = useState(1);

  return (
    <ChapterContext.Provider value={{ curChapter, setCurChapter }}>
      <Split sizes={[25, 75]} direction="horizontal" className="split-flex">
        <Catalogue />
        <Learn />
      </Split>
    </ChapterContext.Provider>
  );
}

function Catalogue() {
  return (
    <div className="Catalogue">
      <p className="CourseTitle">Intro to Logic</p>
      <ul>
        {chapters
          .filter((c) => c.course == "Logic")
          .map((el, i) => {
            return (
              <li key={i}>
                <p style={{ color: "white" }}>{el.chapter}</p>
              </li>
            );
          })}
      </ul>
      <p>Hello</p>
    </div>
  );
}

function Learn() {
  return (
    <div className="Learn">
      <p>Learn</p>
    </div>
  );
}

export default Course;
