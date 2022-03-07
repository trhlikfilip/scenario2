import React from 'react';
import './Header.css'
import img1 from './scenario_image1.PNG';
import img2 from './scenario_image2.PNG';
import img3 from './scenario_image3.PNG';


function Header() {
    return (
        <div className="header">
            <div className="header_button">
                <h>Logo</h>
                <h>  About</h>
                <h>  Learn</h>
            </div>
            <div className="header_image">
                <div className="header_content">
                    <img className="image1" src={img1}/>
                    <h1>Intro to Linear Algebra</h1>
                    <h2>Learn the basics of Linear Algebra like matrix multiplication,
                    determinants, and so on with visualizations</h2>
                </div>
                <div className="header_content">
                    <img className="image2" src={img2}/>
                    <h1>Predicate Logic with AI</h1>
                    <h2>Learn the negation and syllogism with the power of our finetuned GPT-3</h2>
                </div>
                <div className="header_content">
                    <img className="image3" src={img3}/>
                    <h1>TBC</h1>
                    <h2>More engaging courses to be added</h2>
                </div>
            </div>
        </div>
    );
}


export default Header;