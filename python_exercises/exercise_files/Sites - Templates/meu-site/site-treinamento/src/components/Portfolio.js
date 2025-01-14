import { useState } from 'react';
import { Linkedin, Github, Mail, ExternalLink } from 'lucide-react';

const DecorativeShapes = () => (
  <>
    {/* Formas Lado Esquerdo */}
    <div className="fixed left-0 top-0 h-full w-24 pointer-events-none" style={{ zIndex: -1 }}>
      <svg className="h-full w-full" viewBox="0 0 100 800">
        {/* Círculos */}
        <circle cx="30" cy="100" r="15" fill="#F2496B" opacity="0.6" />
        <circle cx="70" cy="200" r="10" fill="#A880FF" opacity="0.4" />
        <circle cx="40" cy="300" r="20" fill="#DCFF79" opacity="0.5" />
        
        {/* Triângulos */}
        <path d="M20 400 L40 440 L0 440 Z" fill="#F2496B" opacity="0.5" />
        <path d="M60 500 L80 530 L40 530 Z" fill="#A880FF" opacity="0.4" />
        
        {/* Formas Orgânicas */}
        <path d="M30 600 Q45 580 60 600 T90 600 Q75 620 60 600 T30 600" fill="#DCFF79" opacity="0.6" />
        <path d="M10 700 Q40 670 70 700 T40 730 Q10 700 40 670" fill="#F2496B" opacity="0.4" />
      </svg>
    </div>

    {/* Formas Lado Direito */}
    <div className="fixed right-0 top-0 h-full w-24 pointer-events-none" style={{ zIndex: -1 }}>
      <svg className="h-full w-full" viewBox="0 0 100 800">
        {/* Formas Orgânicas */}
        <path d="M70 100 Q85 80 100 100 T70 120 Q55 100 70 80" fill="#A880FF" opacity="0.5" />
        <path d="M50 200 Q65 180 80 200 T50 220 Q35 200 50 180" fill="#DCFF79" opacity="0.4" />
        
        {/* Círculos */}
        <circle cx="60" cy="300" r="12" fill="#F2496B" opacity="0.5" />
        <circle cx="80" cy="400" r="15" fill="#A880FF" opacity="0.6" />
        
        {/* Triângulos */}
        <path d="M40 500 L60 540 L20 540 Z" fill="#DCFF79" opacity="0.5" />
        <path d="M70 600 L90 630 L50 630 Z" fill="#F2496B" opacity="0.4" />
        
        {/* Forma Orgânica Adicional */}
        <path d="M60 700 Q75 680 90 700 T60 720 Q45 700 60 680" fill="#A880FF" opacity="0.5" />
      </svg>
    </div>
  </>
);

const Portfolio = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const projects = [
    {
      title: "Projeto 1",
      description: "Um BOT que resume dados da ferramenta de suporte quando fecha a semana",
      tags: ["Python", "PowerBI", "Lark"],
      link: "#",
      media: "/projects/projeto1.png",
      mediaType: "image",
      bgColor: "#F2496B"
    },
    {
      title: "Projeto 2",
      description: "Um modelo de PowerPoint adaptado ao BrandBook do Wellhub",
      tags: ["PowerPoint", "Canva", "Asana"],
      link: "#",
      media: "/projects/projeto5.gif",
      mediaType: "gif",
      bgColor: "#A880FF"
    },
    {
      title: "Projeto 3",
      description: "Exercício de Dashboard de gráfico dinâmico",
      tags: ["PowerBI", "MySQL", "Excel"],
      link: "#",
      media: "/projects/projeto6.mp4",
      mediaType: "video",
      bgColor: "#DCFF79"
    }
  ];

  return (
    <div className="min-h-screen bg-gray-50 relative">
      <DecorativeShapes />
      
      {/* Rest of the component remains the same */}
      <nav className="bg-white shadow-md fixed w-full z-10 rounded-b-lg border border-gray-200">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <span className="text-4xl font-bold text-gray-800">Wellhub Interview</span>
            </div>
            
            <div className="hidden md:flex items-center space-x-8">
              <a href="#home" className="text-gray-600 hover:text-gray-900">Home</a>
              <a href="#sobre" className="text-gray-600 hover:text-gray-900">Sobre</a>
              <a href="#projetos" className="text-gray-600 hover:text-gray-900">Projetos</a>
              <a href="#contato" className="text-gray-600 hover:text-gray-900">Contato</a>
            </div>

            <div className="md:hidden flex items-center">
              <button onClick={() => setIsMenuOpen(!isMenuOpen)} className="p-2">
                {isMenuOpen ? (
                  <span className="text-2xl">×</span>
                ) : (
                  <span className="text-2xl">☰</span>
                )}
              </button>
            </div>
          </div>
        </div>

        {isMenuOpen && (
          <div className="md:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1 bg-white">
              <a href="#home" className="block px-3 py-2 text-gray-600 hover:text-gray-900">Home</a>
              <a href="#sobre" className="block px-3 py-2 text-gray-600 hover:text-gray-900">Sobre</a>
              <a href="#projetos" className="block px-3 py-2 text-gray-600 hover:text-gray-900">Projetos</a>
              <a href="#dúvidas" className="block px-3 py-2 text-gray-600 hover:text-gray-900">Contato</a>
            </div>
          </div>
        )}
      </nav>

      <section id="home" className="pt-20 pb-10 px-4">
        <div className="max-w-7xl mx-auto mt-16 text-center border rounded-lg p-8 bg-white">
          <h1 className="text-5xl font-bold text-gray-900 mb-4">Olá, eu sou o Matheus Cornedi! </h1>
          <p className="text-xl text-gray-600 mb-8">Global Training Analyst</p>
          <div className="flex justify-center space-x-4">
            <a href="https://github.com/KogyDev" target="_blank" className="p-2 text-gray-600 hover:text-gray-900">
              <Github size={24} />
            </a>
            <a href="https://www.linkedin.com/in/matheus-cornedi-614224213/" target="_blank" className="p-2 text-gray-600 hover:text-gray-900">
              <Linkedin size={24} />
            </a>
            <a href="mailto:matheus.r.cornedi@gmail.com" className="p-2 text-gray-600 hover:text-gray-900">
              <Mail size={24} />
            </a> 
          </div>
        </div>
      </section>

      <section id="sobre" className="py-20 bg-white px-4">
        <div className="max-w-3xl mx-auto border rounded-lg p-8 bg-white shadow-lg">
          <h2 className="text-3xl font-bold text-gray-900 mb-8 text-center">Sobre a página</h2>
          <p className="text-gray-600 mb-6">
            Aqui estão alguns projetos que fiz nos ultimos meses que impactaram positivamente o dia-
            Com experiência em desenvolvimento de treinamentos e análise de dados, meu objetivo é facilitar as análises de treinamento e oferecer melhor suporte.
          </p>
          <p className="text-gray-600">
            O site foi feito com React, Nodejs, HTML e CSS.
          </p>
        </div>
      </section>

      <section id="projetos" className="py-20 px-4 bg-gray-50">
        <div className="max-w-7xl mx-auto">
          <h2 className="text-5xl font-bold text-gray-900 mb-12 text-center">Meus Projetos</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {projects.map((project, index) => (
              <div 
                key={index} 
                className="rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow border"
                style={{ backgroundColor: project.bgColor }}
              >
                {project.mediaType === 'image' && (
                    <a href={project.media} target="_blank" rel="noopener noreferrer">
    <img src={project.media} alt={project.title} className="w-full h-48 object-cover rounded-lg mb-4" />
                    </a>
                )}
                {project.mediaType === 'gif' && (
                    <a href={project.media} target="_blank" rel="noopener noreferrer">
                    <img src={project.media} alt={project.title} className="w-full h-48 object-cover rounded-lg mb-4" />
                  </a>            
                )}
                {project.mediaType === 'video' && (
                    
                  <video controls className="w-full h-48 object-cover rounded-lg mb-4">
                    <source src={project.media} type="video/mp4" />
                  </video>
                )}
                <h3 className="text-xl font-bold mb-2 px-4 py-2 bg-white/70 text-black rounded-lg">{project.title}</h3>
                <p className="font-bold mb-4">{project.description}</p>
                <div className="flex flex-wrap gap-2 mb-4">
                  {project.tags.map((tag, tagIndex) => (
                    <span key={tagIndex} className="px-3 py-1 bg-white/50 font-bold rounded-full text-sm">
                      {tag}
                    </span>
                  ))}
                </div>
                <a href={project.link} target="_blank" className="inline-flex items-center text-black hover:opacity-75">
                  Ver projeto <ExternalLink size={16} className="ml-1" />
                </a>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section id="dúvidas" className="py-20 bg-white px-4">
        <div className="max-w-3xl mx-auto text-center border rounded-lg p-8 bg-white shadow-lg">
          <h2 className="text-3xl font-bold text-gray-900 mb-8">Vamos Conversar?</h2>
          <p className="text-gray-600 mb-8">
            Caso tenha alguma dúvida, pode chamar! :D
          </p>
        </div>
      </section>
    </div>
  );
};

export default Portfolio;
