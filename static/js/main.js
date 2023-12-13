document.addEventListener('DOMContentLoaded', function() {

    const burgerMenuButton = document.querySelector('.burger-menu');
    const burgerMenuLinks = document.querySelector('.main-menu-links');

    burgerMenuButton.addEventListener('click', function() {
    burgerMenuButton.classList.toggle('button-active');
    burgerMenuLinks.classList.toggle('mobile-active');
    });

// Get the current URL slug
const currentSlug = window.location.pathname;

// Get all the navigation links
const navLinks = document.querySelectorAll('.nav-link');

// Loop through the links and check if their href slug matches the current slug
navLinks.forEach(link => {
  const linkHref = link.getAttribute('href');
  const linkSlug = linkHref.replace(/^.*\/\/[^\/]+/, ''); // Remove domain from link slug

  if (linkHref === '/' && currentSlug === '/') {
    // If on the homepage and the link is the "Home" link, mark the link as active
    link.classList.add('active');
  } else if (linkSlug !== '/' && currentSlug.startsWith(linkSlug)) {
    // If the link href slug is not "/" and the current slug starts with the link href slug, mark the link as active
    link.classList.add('active');
  } else if (linkSlug === '/blog' && currentSlug.startsWith('/blog/')) {
    // If the link is the "Blog" link or a sub-page of the "Blog" link, mark the link as active
    link.classList.add('active');
  } else if (linkSlug === '/portfolio' && currentSlug.startsWith('/portfolio/')) {
    // If the link is the "Portfolio" link or a sub-page of the "Portfolio" link, mark the link as active
    link.classList.add('active');
  }
});


    // Select all links with the class "scroll-link"
    const scrollLinks = document.querySelectorAll('.scroll-link');
    
    // Loop through each link and add a click event listener
    scrollLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            // Prevent the default link behavior
            event.preventDefault();
            
            // Get the target element that the link points to
            const target = document.querySelector(link.getAttribute('href'));
            
            // Calculate the distance from the top of the page to the target element
            const targetPosition = target.offsetTop;
            
            // Set the duration of the scroll animation (in milliseconds)
            const duration = 1000;
            
            // Create a scroll animation
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth',
                duration: duration
            });
        });
    });
});

window.addEventListener('load', () => {
  
      function scrollSpy() {
        const fromTop = window.scrollY;
        const links = document.querySelectorAll('.project-stages-nav a');
        let activeLink = null;
      
        document.querySelectorAll('.design-process-step').forEach(section => {
          const top = section.offsetTop;
          const height = section.offsetHeight;
      
          if (fromTop >= top - (window.innerHeight / 2) && fromTop < top + height) {
            activeLink = document.querySelector(`.project-stages-nav a[href="#${section.id}"]`);
            return;
          }
        });
      
        links.forEach(link => {
          if (link === activeLink) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
      
      
      window.addEventListener('load', () => {
        scrollSpy();
      });
      
      window.addEventListener('scroll', () => {
        scrollSpy();
      });
      
      document.querySelectorAll('.scroll-link').forEach(link => {
        link.addEventListener('click', event => {
          event.preventDefault();
          const targetId = link.hash;
          const targetElement = document.querySelector(targetId);
          const targetOffsetTop = targetElement.offsetTop;
          window.scrollTo({
            top: targetOffsetTop,
            behavior: 'smooth'
          });
        });
      });
});