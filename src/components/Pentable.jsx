import React from 'react'
import Sdata from './Sdata';
import '../App.css';

function Pentable() {
    return (
        <>
            <table class="content-table">
                <thead>
                    <tr>
                        <th>User</th>
                        <th></th>
                        <th>Rank level <i class="fa-solid fas fa-sort"></i></th>
                        <th>Trigger reason</th>
                        <th>In queue for <i class="fa-solid fas fa-sort"></i></th>
                        <th>Date added on <i class="fa-solid fas fa-sort"></i></th>
                        <th>Previously reviewed</th>
                    </tr>
                </thead>
                <tbody>


                    <tr>
                        <td>
                            <div class="tr1">
                                <h4>{Sdata[0].username}</h4>
                                <p>{Sdata[0].penmail}</p>
                            </div>
                        </td>
                        <td><i class="fa-solid fa-arrow-up-right-from-square"></i></td>
                        <td class="medtxt"><i class="fa-solid fa-circle medicircle"></i>{Sdata[0].risklvl}</td>
                        <td class="nrmtxt">{Sdata[0].queuepen}</td>
                        <td class="nrmtxt">{Sdata[0].pendays}</td>
                        <td class="lgtxt">{Sdata[0].pendate}</td>
                        <td>
                            <div class="tr1">
                                <h4>{Sdata[0].penchcek}</h4>
                                <p>{Sdata[0].pendatelst}</p>
                            </div>
                        </td>
                    </tr>

                   


                    <tr>
                        <td>
                            <div class="tr1">
                                <h4>{Sdata[1].username}</h4>
                                <p>{Sdata[1].penmail}</p>
                            </div>
                        </td>
                        <td><i class="fa-solid fa-arrow-up-right-from-square"></i></td>
                        <td class="higtxt"><i class="fa-solid fa-circle higcircle"></i>{Sdata[1].risklvl}</td>
                        <td class="nrmtxt">{Sdata[1].queuepen}</td>
                        <td class="nrmtxt">{Sdata[1].pendays}</td>
                        <td class="lgtxt">{Sdata[1].pendate}</td>
                        <td class="nrmtxt">{Sdata[1].penchcek}</td>
                    </tr>

                    <tr>
                        <td>
                            <div class="tr1">
                                <h4>{Sdata[2].username}</h4>
                                <p>{Sdata[2].penmail}</p>
                            </div>
                        </td>
                        <td><i class="fa-solid fa-arrow-up-right-from-square"></i></td>
                        <td class="lowtxt"><i class="fa-solid fa-circle lowcircle"></i>{Sdata[2].risklvl}</td>
                        <td class="nrmtxt">{Sdata[2].queuepen}</td>
                        <td class="nrmtxt">{Sdata[2].pendays}</td>
                        <td class="lgtxt">{Sdata[2].pendate}</td>
                        <td class="nrmtxt">{Sdata[2].penchcek}</td>
                    </tr>

                    <tr>
                        <td>
                            <div class="tr1">
                            <h4>{Sdata[3].username}</h4>
                                <p>{Sdata[3].penmail}</p>
                            </div>
                        </td>
                        <td><i class="fa-solid fa-arrow-up-right-from-square"></i></td>
                        <td class="higtxt"><i class="fa-solid fa-circle higcircle"></i>{Sdata[3].risklvl}</td>
                        <td class="nrmtxt">{Sdata[3].queuepen}</td>
                        <td class="nrmtxt">{Sdata[3].pendays}</td>
                        <td class="lgtxt">{Sdata[3].pendate}</td>
                        <td>
                            <div class="tr1">
                                <h4>{Sdata[3].penchcek}</h4>
                                <p>{Sdata[3].pendatelst}</p>
                            </div>
                        </td>
                    </tr>

                    <tr>
                        <td>
                            <div class="tr1">
                            <h4>{Sdata[4].username}</h4>
                                <p>{Sdata[4].penmail}</p>
                            </div>
                        </td>
                        <td><i class="fa-solid fa-arrow-up-right-from-square"></i></td>
                        <td class="lowtxt"><i class="fa-solid fa-circle lowcircle"></i>{Sdata[4].risklvl}</td>
                        <td class="nrmtxt">{Sdata[4].queuepen}</td>
                        <td class="nrmtxt">{Sdata[4].pendays}</td>
                        <td class="lgtxt">{Sdata[4].pendate}</td>
                        <td>
                            <div class="tr1">
                                <h4>{Sdata[4].penchcek}</h4>
                                <p>{Sdata[4].pendatelst}</p>
                            </div>
                        </td>
                    </tr>

                    <tr>
                        <td>
                            <div class="tr1">
                            <h4>{Sdata[5].username}</h4>
                                <p>{Sdata[5].penmail}</p>
                            </div>
                        </td>
                        <td><i class="fa-solid fa-arrow-up-right-from-square"></i></td>
                        <td class="lowtxt"><i class="fa-solid fa-circle lowcircle"></i>{Sdata[5].risklvl}</td>
                        <td class="nrmtxt">{Sdata[5].queuepen}</td>
                        <td class="nrmtxt">{Sdata[5].pendays}</td>
                        <td class="lgtxt">{Sdata[5].pendate}</td>
                        <td>
                            <div class="tr1">
                                <h4>{Sdata[5].penchcek}</h4>
                                <p>{Sdata[5].pendatelst}</p>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </>
    )
}

export default Pentable
