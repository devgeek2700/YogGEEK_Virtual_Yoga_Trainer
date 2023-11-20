import React from 'react';
import '../App.css';


function Sidemenu() {


    const finalnav = ()=>{
        let monttxt = document.getElementById('monttxt');
        let montlist = document.getElementById('montlist');
      
        monttxt.style.color = "blue";
        montlist.style.backgroundColor = "#d3d2fa";
    }

    const normnav = ()=>{
        let monttxt = document.getElementById('monttxt');
        let montlist = document.getElementById('montlist');
      
        monttxt.style.color = "black";
        montlist.style.backgroundColor = "#fff";
    }
      
  return (
    <>
      <div class="col1">
                <h1 id="logo">LOGO HERE</h1>
                <ol>
                    <li><a href="#">Overview</a></li>
                    <li><a href="#">Onboarding</a></li>
                    <li id="montlist"><a href="#" onClick={finalnav} onDoubleClick={normnav} id="monttxt">Montioring</a></li>
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
    </>
  )
}

export default Sidemenu
