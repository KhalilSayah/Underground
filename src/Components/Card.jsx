import React, { useState } from "react";
import './Card.css'

function Card({id, title, imageUrl, Link, adress, proposals}) {
    
    console.log(proposals);
    const [showCardProp, setShowCardProp] = useState(false);
    const [currentCard, setCurrentCard] = useState(null);

    const handleClick = (event) => {
        if (currentCard === title) {
            setShowCardProp(!showCardProp);
        } else {
            setShowCardProp(true);
            setCurrentCard(title);
        }

        // Empêcher la propagation de l'événement click
        event.stopPropagation();
    };

    // Ajoutez une fonction pour gérer le clic sur les éléments de type radio et le bouton "Submit"
    const handleRadioClick = (event) => {
        // Empêcher la propagation de l'événement click
        event.stopPropagation();

        // Placez ici le code pour gérer le clic sur les éléments de type radio
        // ...
    };

    const handleSubmit = (event) => {
        // Empêcher la propagation de l'événement click
        event.stopPropagation();

        // Placez ici le code pour gérer le clic sur le bouton "Submit"
        // ...
    };

    return (
        <>
            <div className="card-container" onClick={handleClick}>
                <div className="card-title">
                    <h5 className="text-white">{title}</h5>
                </div>
                {showCardProp && (
                    <>
                        <form>
                            <div className="row" id="rowCard">
                                <div className="col-md-4">
                                    <div className="image-container">
                                        <img src={imageUrl} alt="" />
                                    </div>
                                </div>
                                <div className="col-md-8">
                                    <p className="card-link text-white">Adresse : {adress}</p>
                                    <p className="card-link text-white">id : {id}</p>
                                    <a href={Link} className="card-link text-white" >Link Tweet</a>
                                    <div className="card-prop">
                                    {Array.isArray(proposals) ? (
                                        proposals.map(([text, count], index) => (
                                        <div className="form-check" key={index}>
                                            <input
                                            className="form-check-input"
                                            type="radio"
                                            name="flexRadioDefault"
                                            id={`flexRadioDefault${index}`}
                                            checked={currentCard === title && showCardProp}
                                            onClick={handleRadioClick}
                                            />
                                            <label className="form-check-label text-white" htmlFor={`flexRadioDefault${index}`}>
                                            {text}
                                            </label>
                                        </div>
                                        ))
                                    ) : (
                                        <p>No proposals available.</p>
                                    )}
                                    </div>
                                    <div className="col-12">
                                        <button className="btn btn-lg" id="submit" type="submit" onClick={handleSubmit}>Submit</button>
                                    </div>
                                </div>
                                
                            </div>

                        </form>
                    </>
                )}
            </div>
        </>
    );
}

export default Card;
