const updateGreeting = () => {
  const now = new Date();
  const hour = now.getHours();
  const greeting = hour < 12 ? "Good Morning" : hour < 18 ? "Good Afternoon" : "Good Evening";

  document.getElementById("msg").innerText = greeting;
  document.getElementById("time").innerText = now.toLocaleString();
};

updateGreeting();
setInterval(updateGreeting, 1000);
