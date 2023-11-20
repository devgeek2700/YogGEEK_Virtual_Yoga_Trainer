import React from 'react'
import './App.css';


function Sidebarmenu() {
    
    return (
        <>
        <div class="row">
            <div class="col1">
                <h1 id="logo">LOGO HERE</h1>
                <ol>
                    <li><a href="#">Overview</a></li>
                    <li><a href="#">Onboarding</a></li>
                    <li><a href="#">Montioring</a></li>
                    <li><a href="#">Flagging</a></li>
                    <li><a href="#">Source of Income</a></li>
                    <li><a href="#">UAR</a></li>

                    <div class="sideimgbox">
                        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSLWm3MxqL0RDugL-oMVzOx1fusc8PGRodhbQ&usqp=CAU"
                            class="sideimg" alt=""/>
                        <div>
                            <h4>Elon Musk</h4>
                            <p>elon@twitter.com</p>
                        </div>
                    </div>
                </ol>
            </div>
        </div>

        </>
    )
}

export default Sidebarmenu;
