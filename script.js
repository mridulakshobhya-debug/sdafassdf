// Intersection Observer: reveal on scroll
const observer = new IntersectionObserver((entries)=>{
  entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in-view'); observer.unobserve(e.target);} });
}, {threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));

// Simple parallax on mouse move for hero cards
const heroCards = document.querySelectorAll('.tilt, .pop');
document.addEventListener('mousemove', (e)=>{
  const { innerWidth:w, innerHeight:h } = window;
  const rx = ((e.clientY - h/2) / h) * 6;
  const ry = ((e.clientX - w/2) / w) * -6;
  heroCards.forEach(card=>{ card.style.transform = `perspective(1000px) rotateX(${rx}deg) rotateY(${ry}deg)`; });
});
document.addEventListener('mouseleave', ()=>{
  heroCards.forEach(card=>{ card.style.transform = ''; });
});

// Current year
document.getElementById('year').textContent = new Date().getFullYear();

// Make all .btn elements clickable with a demo alert
// Remove demo alert for .btn elements so navigation work
// Business Idea Generator logic
const ideas = [
  "🎨 Start a custom sticker design business",
  "🍪 Sell homemade cookies with fun packaging",
  "📚 Write and sell your own comic book series",
  "🐾 Create pet toys from recycled materials",
  "🎧 Host a podcast for kids, by kids!",
  "🌱 Launch a mini plant growing kit business",
  "🎁 Design surprise gift boxes for birthdays",
  "👕 Sell hand-painted T-shirts or tote bags",
  "📸 Offer photo booth services for kids' parties",
  "🚲 Start a weekend bike cleaning service",
  "🧼 Create and sell colorful bath bombs",
  "🧁 Host a cupcake-of-the-month club",
  "📒 Make DIY journals and planners for students",
  "💌 Sell handmade greeting cards for all seasons",
  "🖌️ Offer face painting at events or markets",
  "🎨 Start a custom art class for kids"
  //Activities Generator
];
const generateIdeaBtn = document.getElementById('generateIdeaBtn');
if (generateIdeaBtn) {
  generateIdeaBtn.onclick = function() {
    const randomIndex = Math.floor(Math.random() * ideas.length);
    const idea = ideas[randomIndex];
    document.getElementById("ideaBox").textContent = idea;
  };
}
// Live Dashboard Demo: Animate numbers
function animateDashboard() {
  // Select dashboard stat elements
  const profitEl = document.querySelector('.pop .feature.card:nth-child(1) h4');
  const customersEl = document.querySelector('.pop .feature.card:nth-child(2) h4');
  const streakEl = document.querySelector('.pop .feature.card:nth-child(3) h4');
  if (!profitEl || !customersEl || !streakEl) return;

  // Initial values
  let profit = 1240;
  let customers = 86;
  let streak = 14;

  setInterval(() => {
    // Randomly change values for demo
    profit += Math.floor(Math.random() * 40 - 20); // -20 to +19
    customers += Math.floor(Math.random() * 6 - 3); // -3 to +2
    streak = Math.max(1, streak + (Math.random() > 0.7 ? 1 : 0));
    // Clamp values
    profit = Math.max(1000, profit);
    customers = Math.max(10, customers);
    // Update DOM
    profitEl.textContent = `₹ ${profit.toLocaleString()}`;
    customersEl.textContent = customers;
    streakEl.textContent = `${streak} days`;
  }, 2500);
}
// Run animation on homepage only
if (document.querySelector('.pop .feature.card')) animateDashboard();