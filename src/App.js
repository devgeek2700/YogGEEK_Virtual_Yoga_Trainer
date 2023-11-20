import './App.css';
import Sidemenu from './components/Sidemenu';
import Pentable from './components/Pentable';
import Dropdown from './components/Dropdown';
import Compltable from './components/Compltable';



function App() {
    
    const ischcked = () => {
        let formBtn = document.querySelector('.formBtn');
        let clsccbtn = document.querySelector('#clsccbtn');

        clsccbtn.style.color = "white";
        formBtn.style.backgroundColor = "blue";
    }

    return (
        <>
            <div class="cont">
                {/* Left side */}

                <div class="row">

                    <Sidemenu />


                    {/* Right side */}
                    <div class="col2">
                        <div class="subcol">
                            <div class="scol1">
                                <h2>Montioring</h2>
                            </div>
                            <div class="scol2">
                                <div class="pencom">
                                    <div class="pen1" id="pendbox">
                                        <li id="penpara">Pending</li>
                                    </div>
                                    <div class="pen2" id="compbox">
                                        <li id="compbtn">Completed</li>
                                    </div>

                                </div>
                                <div class="closebtn">

                                    <div class="closeBtn">
                                        <i class="fa-regular fa-circle-xmark"></i>
                                        <a href="#popup-box">
                                            close account
                                        </a>
                                    </div>
                                    <div id="popup-box" class="modal">
                                        <div class="content">
                                            <h1>
                                                close account
                                            </h1>
                                            <form>
                                                <div class="form-group">
                                                    <label for="exampleFormControlInput1">Email</label>
                                                    <input type="email" class="form-control" id="exampleFormControlInput1" />
                                                </div>

                                                <div class="form-group">
                                                    <div class="radiorow">


                                                        <label for="exampleFormControlInput1" id="uartxt">Want to file UAR</label>

                                                        <div class="radiobtnbox">

                                                            <div class="form-check form-check-inline radioBtn">
                                                                <div class="rb1">
                                                                    <input type="radio" name="coffee" value="yes" /> Yes
                                                                </div>
                                                                <div>
                                                                    <input type="radio" name="coffee" value="yes" /> No
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>

                                                </div>
                                                <div class="form-group">
                                                    <label for="exampleFormControlSelect1">Reason</label>
                                                    <select class="form-control" id="exampleFormControlSelect1">
                                                        <option>Flagging logics triggered</option>
                                                        <option>Flagging logics triggered1</option>
                                                        <option>Flagging logics triggered2</option>
                                                        <option>Flagging logics triggered3</option>
                                                        <option>Flagging logics triggered4</option>
                                                    </select>

                                                </div>
                                                <div class="form-group">
                                                    <label for="exampleFormControlTextarea1">Note</label>
                                                    <textarea class="form-control" id="exampleFormControlTextarea1"
                                                        rows="3"></textarea>
                                                </div>

                                                <div class="lastfbox">
                                                    <div class="chargefee">
                                                        <input type="radio" name="coffee" value="yes" id="chargetxt" onClick={ischcked} /> Charge closure fee
                                                    </div>
                                                    <div class="formBtn">
                                                        <a href="#" class="last-form-btn" id='clsccbtn'>
                                                            Close Account
                                                        </a>
                                                    </div>
                                                </div>
                                            </form>
                                            <a href="#" class="box-close">
                                                ×
                                            </a>
                                        </div>
                                    </div>

                                </div>

                            </div>
                            <div class="scol3">
                                <div class="barbox">
                                    <div class="bcol1">
                                        <div class="brow">
                                            <i class="fa-solid fa-magnifying-glass"></i>
                                            <input type="text" name="" id="" placeholder="Search" />
                                        </div>
                                    </div>

                                    <div class="bcol2">

                                        <Dropdown />

                                    </div>

                                    <div class="bcol3">
                                        <div class="select-menu active select-menu1">
                                            <div class="select-btn select-btn1">
                                                <span class="sBtn-text sBtn-text1">Risk level</span>
                                                <i class="fa-solid fa-angle-up" id="arrowUp"></i>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>


                        <div class="scol4" id="div4">
                            <Pentable />
                        </div>


                        <div class="scol5" id="div5">
                            <Compltable />
                        </div>
                    </div>
                </div>
            </div>

        </>
    );
}

export default App;
