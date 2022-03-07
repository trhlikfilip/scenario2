import "./Learn.css";

function Learn(props) {
  const { question, choices } = props.quiz;

  return (
    <div
      className="Learn"
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div className="QuestionContainer">
        <p className="Question">Q. {question}</p>
        <ul>
          {choices.map((choice, i) => {
            return (
              <li key={i}>
                <button
                  onClick={() => console.log(choice)}
                  className="ChoiceButton"
                >
                  <p className="ChoiceText">
                    {i + 1}. {choice}
                  </p>
                </button>
              </li>
            );
          })}
        </ul>
      </div>
    </div>
  );
}

export default Learn;
