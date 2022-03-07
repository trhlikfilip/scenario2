import Split from "react-split";
import "./Course.css";
import ChapterContext from "./ChapterContext.js";
import { useState } from "react";
import Catalogue from "./Catalogue";
import Learn from "./Learn";
import "typeface-anonymous-pro";

function Course() {
  const [curChapter, setCurChapter] = useState(1);

  const quiz = {
    question: "I hate dogs and I love cats",
    choices: [
      "I hate dogs or I don’t love cats",
      "I don’t hate dogs or I love cats",
      "I don’t hate dogs or I don’t love cats",
      "I don’t hate dogs and I don’t love cats",
    ],
  };

  return (
    <ChapterContext.Provider value={{ curChapter, setCurChapter }}>
      <Split sizes={[25, 75]} direction="horizontal" className="split-flex">
        <Catalogue />
        <Learn quiz={quiz} />
      </Split>
    </ChapterContext.Provider>
  );
}

export default Course;
