import React from 'react';
import './Landing.css';
import image4 from './scenario_image4.png';

function Landing() {
    return(
        <div>
            <div className="top_button">
                <span className="top_button1">Logo</span>
                <span className="top_button2">About</span>
                <span className="top_button3">Learn</span>
            </div>

            <div className="description">
                <div className="description_context">
                    <span className="description_title">Interactive Courses</span>
                    <span className="description_text">Today, there is an almost unlimited number of educational 
                    apps and programs on the internet with their own weaknesses. <br/><br/>
                    Therefore, our team has decided to pursue an app that can procedurally 
                    generate new questions for its users. <br/><br/>
                    Provide more comprehensive way of practising their knowledge.</span>
                </div>
                <img className="description_image" src={image4}/>
            </div>
        </div>
    )
}

export default Landing;