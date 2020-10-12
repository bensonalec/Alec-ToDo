// import React from "react";
import "./List.css";
import { useAppContext } from "../libs/contextLib";

import React, { Component } from "react";


class List extends Component {

  
  // test() {
  //   const { userHasAuthenticated } = useAppContext();
  //   console.log("IN")
  // }
  state = {
    listitems: [["Apple","1"], ["Pear","2"], ["Avocado","3"]],
  };

  render() {
    return (
      <React.Fragment>
        <ul className="list-group">
          {this.state.listitems.map(listitem => (
            <li className="list-group-item list-group-item-primary">
              {listitem[0]}
              <li className="list-group-item list-group-item-secondary">
                {listitem[1]}
              </li>
            </li>
          ))}
        </ul>
      </React.Fragment>
    );
  }
}
export default List;
