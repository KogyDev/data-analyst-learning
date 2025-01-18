import React, { useState, useEffect } from 'react';
import minhaFoto from '../assets/images/eu.png';

const Portfolio = () => {
  const [expandedProject, setExpandedProject] = useState(null); // Estado para controlar a expansão

  useEffect(() => {
    const handleScroll = () => {
      const elements = document.querySelectorAll('.fade-in');
      elements.forEach(element => {
        const rect = element.getBoundingClientRect();
        const isVisible = (rect.top <= window.innerHeight * 0.75);
        if (isVisible) {
          element.classList.add('visible');
        }
      });
    };

    window.addEventListener('scroll', handleScroll);
    window.addEventListener('load', handleScroll);

    return () => {
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('load', handleScroll);
    };
  }, []);

  const scrollToSection = (e, id) => {
    e.preventDefault();
    document.querySelector(id).scrollIntoView({
      behavior: 'smooth'
    });
  };

  return (
    <div className="min-h-screen bg-gray-100 relative">
      {/* Escondi o menu Home/Projetos */}
      {/* Navegação */}
      <nav className="hidden">
        <ul className="list-none">
          <li className="my-2">
            <a 
              href="#home" 
              onClick={(e) => scrollToSection(e, '#home')}
              className="text-gray-800 text-lg font-medium px-4 py-1 rounded-2xl hover:bg-gray-100 hover:text-blue-600 transition-colors block"
            >
              Home
            </a>
          </li>
          <li className="my-2">
            <a 
              href="#projects" 
              onClick={(e) => scrollToSection(e, '#projects')}
              className="text-gray-800 text-lg font-medium px-4 py-1 rounded-2xl hover:bg-gray-100 hover:text-blue-600 transition-colors block"
            >
              Projetos
            </a>
          </li>
        </ul>
      </nav>

      {/* Ícones Sociais (Diminuídos) */}
      <div className="fixed top-5 right-5 z-50">
        <a href="https://github.com/KogyDev" target="_blank" rel="noopener noreferrer" className="ml-4 text-gray-800 hover:text-blue-600 transition-colors">
          <i className="fab fa-github text-6xl"></i> {/* Reduzido ícone */}
        </a>
        <a href="https://www.linkedin.com/in/matheus-cornedi-614224213/" target="_blank" rel="noopener noreferrer" className="ml-4 text-gray-800 hover:text-blue-600 transition-colors">
          <i className="fab fa-linkedin text-6xl"></i> {/* Reduzido ícone */}
        </a>
        <a href="mailto:matheus.r.cornedi@gmail.com" className="ml-4 text-gray-800 hover:text-blue-600 transition-colors">
          <i className="fas fa-envelope text-6xl"></i> {/* Reduzido ícone */}
        </a>
      </div>

      {/* Seção Home */}
      <section id="home" className="min-h-screen p-20 flex items-center justify-center gap-12 flex-wrap fade-in opacity-0 relative">
        {/* Esfera de fundo */}
        <div className="absolute w-[320px] h-[320px] rounded-full bg-[#F2496B]" style={{ zIndex: 1 }}></div> {/* Esfera sólida de fundo */}

        {/* Foto de perfil na frente */}
        <div className="relative w-[270px] h-[270px] z-10"> {/* Tamanho da foto */}
          <img
            src={minhaFoto} alt="Foto de Perfil"
            className="absolute w-full h-full rounded-full object-cover top-[50%] left-[50%] transform -translate-x-[50%] -translate-y-[50%]" // Foto centralizada
          />
        </div>
      </section>

      {/* Texto abaixo da foto */}
      <div className="text-center mt-8">
        <h1 className="text-8xl mb-5">Oi, eu sou Matheus Cornedi!</h1> {/* Aumentei a fonte */}
      </div>

      {/* Frase com fundo da cor da forma blob e texto branco */}
      <div className="text-center mt-4">
        <p className="text-3xl font-bold text-white inline-block py-2 px-4 rounded-xl" style={{ backgroundColor: '#F2496B' }}>
          Aqui estão alguns projetos que demonstram meu trabalho e dedicação.
        </p>
      </div>

      {/* Formas "blob" aleatórias */}
      <div className="absolute left-0 top-0 w-32 h-32 bg-[#F2496B] rounded-full transform -translate-y-[50%] -translate-x-[50%]" style={{clipPath: "polygon(50% 0%, 100% 10%, 100% 50%, 50% 100%, 0% 50%, 0% 10%)"}} />
      <div className="absolute right-0 top-0 w-32 h-32 bg-[#A880FF] rounded-full transform -translate-y-[50%] translate-x-[50%]" style={{clipPath: "polygon(50% 0%, 100% 10%, 100% 50%, 50% 100%, 0% 50%, 0% 10%)"}} />
      <div className="absolute left-0 bottom-0 w-32 h-32 bg-[#DCFF79] rounded-full transform -translate-y-[50%] translate-x-[50%]" style={{clipPath: "polygon(50% 0%, 100% 10%, 100% 50%, 50% 100%, 0% 50%, 0% 10%)"}} />

      {/* Seção Projetos */}
      <section id="projects" className="py-24 px-5 fade-in opacity-0">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto">
          {[{ type: 'image', title: 'Projeto 1', src: '/projects/projeto1.png' },
            { type: 'image', title: 'Projeto 2', src: '/projects/projeto2.png' },
            { type: 'image', title: 'Projeto 3', src: '/projects/projeto3.png' },
            { type: 'image', title: 'Projeto 4', src: '/projects/projeto4.png' },
            { type: 'gif', title: 'PowerPoint', src: '/projects/projeto5.gif' },
            { type: 'video', title: 'Vídeo Demo', src: '/projects/video_demo.mp4' }].map((project, index) => (
            <div 
              key={index} 
              className={`bg-white rounded-2xl overflow-hidden shadow-md transform transition-transform hover:scale-105 relative ${expandedProject === index ? 'scale-110 z-10' : ''}`} 
              onClick={() => {
                if (project.type === 'image' || project.type === 'gif') {
                    window.open(project.src, '_blank');
                  }
                  
                if (project.type === 'image') {
                  window.open(project.src, '_blank'); // Para imagens, abrir em nova janela
                }
              }}
            >
              {project.type === 'video' ? (
                <video 
                  controls 
                  className={`w-full h-[350px] object-cover transition-all duration-300 ${expandedProject === index ? 'h-[480px]' : 'h-[350px]'}`}
                >
                  <source src={project.src} type="video/mp4" />
                  Seu navegador não suporta o elemento de vídeo.
                </video>
              ) : project.type === 'gif' ? (
                <img 
                  src={project.src} 
                  alt={project.title}
                  className={`w-full object-cover transition-all duration-300 ${expandedProject === index ? 'h-[480px]' : 'h-[350px]'}`}
                />
              ) : (
                <img 
                  src={project.src} 
                  alt={project.title}
                  className={`w-full object-cover transition-all duration-300 ${expandedProject === index ? 'h-[480px]' : 'h-[350px]'}`}
                />
              )}
              <div className="absolute bottom-0 left-0 right-0 bg-white/90 py-4 text-center font-medium border-t-3 border-blue-600 transition-all duration-300 hover:bg-blue-600 hover:text-white">
                <span className="hover:text-[#F2496B]"> {/* Alterado para cor da esfera */}
                  {project.title}
                </span>
              </div>
            </div>
          ))}

        </div>
      </section>

      {/* Font Awesome */}
      <link 
        rel="stylesheet" 
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
      />

      {/* Fonte Inter Bold */}
      <link 
        rel="stylesheet" 
        href="https://fonts.googleapis.com/css2?family=Inter:wght@700&display=swap" 
      />

      <style jsx global>{`
        .fade-in {
          transition: opacity 0.5s ease-in;
        }
        .fade-in.visible {
          opacity: 1;
        }

        /* Usar a fonte Inter Bold */
        body {
          font-family: 'Inter', sans-serif;
        }
      `}</style>
    </div>
  );
};

export default Portfolio;
