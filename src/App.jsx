import React, { useState, useEffect } from 'react';
import './App.css';
import Card from './Components/Card/';
import Votes from './dumpdata.json';

function App() {
  const itemsPerPage = 8; // Nombre d'éléments à afficher par page
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  useEffect(() => {
    // Calculez le nombre total de pages en fonction du nombre total d'éléments et du nombre d'éléments par page
    setTotalPages(Math.ceil(Votes.length / itemsPerPage));
  }, []);

  const handleNextPage = () => {
    // Passez à la page suivante (à moins qu'il ne s'agisse déjà de la dernière page)
    if (currentPage < totalPages) {
      setCurrentPage((prevPage) => prevPage + 1);
    }
  };

  const handlePrevPage = () => {
    // Passez à la page précédente (à moins qu'il ne s'agisse déjà de la première page)
    if (currentPage > 1) {
      setCurrentPage((prevPage) => prevPage - 1);
    }
  };

  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;
  const visibleVotes = Votes.slice(startIndex, endIndex);

  return (
    <>
      {
        visibleVotes.map((Vote) => (
          <Card
            key={Vote.id}
            title={Vote.data.question}
            imageUrl={Vote.data.image}
            Link={Vote.data.link}
            adress={Vote.address}
            id={Vote.id}
            proposals={Vote.data.proposals}
          />
        ))
      }

      {/* Boutons de pagination */}
      <div>
        <button onClick={handlePrevPage} disabled={currentPage === 1}>Précédent</button>
        <span>Page {currentPage} sur {totalPages}</span>
        <button onClick={handleNextPage} disabled={currentPage === totalPages}>Suivant</button>
      </div>
    </>
  );
}

export default App;
