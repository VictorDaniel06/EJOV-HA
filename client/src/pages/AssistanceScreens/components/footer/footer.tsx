// src/pages/AssistanceScreens/components/footer/footer.tsx
import React from 'react';
import './footer.css';

const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <span className="footer-text">CANAIS DE COMUNICAÇÃO</span>
      <div className="footer-icons">
        {/* Ícones ou placeholders para os canais de comunicação */}
        <div className="footer-icon-placeholder"></div>
        <div className="footer-icon-placeholder"></div>
        <div className="footer-icon-placeholder"></div>
      </div>
    </footer>
  );
};

export default Footer;