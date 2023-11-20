import React from 'react'
import '../App.css';

function Dropdown() {
    const optionMenu = document.querySelector(".select-menu"),
        selectBtn = optionMenu.querySelector(".select-btn"),
        options = optionMenu.querySelectorAll(".option"),
        sBtn_text = optionMenu.querySelector(".sBtn-text");

    selectBtn.addEventListener("click", () =>
        optionMenu.classList.toggle("active")
    );

    options.forEach((option) => {
        option.addEventListener("click", () => {
            let selectedOption = option.querySelector(".option-text").innerText;
            sBtn_text.innerText = selectedOption;

            optionMenu.classList.remove("active");
        });
    });
    return (
        <>
            <div class="select-menu active">
                <div class="select-btn">
                    <span class="sBtn-text">Trigger reason</span>
                    <i class="fa-solid fa-angle-down" id="arrowDn"></i>
                </div>

                <ul class="options">
                    <li class="option">
                        <span class="option-text">Hard flag</span>
                    </li>
                    <li class="option">
                        <span class="option-text">Temp flag</span>
                    </li>
                    <li class="option">
                        <span class="option-text">Restricted unflag</span>
                    </li>
                    <li class="option">
                        <span class="option-text">Un flag</span>
                    </li>
                    <li class="option">
                        <span class="option-text">Reviewed</span>
                    </li>
                </ul>
            </div>
        </>
    )
}

export default Dropdown;
