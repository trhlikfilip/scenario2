import Split from "react-split";
import "./Course.css";
import ChapterContext from "./ChapterContext.js";
import { useContext } from "react";
import chapters from "./chapters";

function selectChapter(id, setCurChapter) {
  setCurChapter(id);
}

function Catalogue() {
  const { curChapter, setCurChapter } = useContext(ChapterContext);

  return (
    <div className="Catalogue">
      <p className="CourseTitle">Practice Negation with AI</p>
      <ul>
        {chapters
          .filter((c) => c.course == "Logic")
          .map((el, i) => {
            return (
              <li key={i}>
                {el.id === curChapter ? (
                  <p className="ChapterText CurrentChapter">{el.chapter}</p>
                ) : (
                  <p
                    onClick={() => selectChapter(el.id, setCurChapter)}
                    className="ChapterText"
                  >
                    {el.chapter}
                  </p>
                )}
              </li>
            );
          })}
      </ul>
      <p className="ChapterText Bottom">Home</p>
    </div>
  );
}

export default Catalogue;
