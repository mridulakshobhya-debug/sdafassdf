from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple knowledge base for Kidpreneur
KIDPRENEUR_FAQ = {
    "what is kidpreneur": "Kidpreneur is a program that helps young people learn entrepreneurship by building real-world projects and businesses.",
    "how do i start": "You can start by joining the Kidpreneur program, picking a business idea, and following the step-by-step roadmap.",
    "what skills will i learn": "You will learn money management, marketing, customer care, product design, and problem-solving skills.",
    "who can join": "Any creative kid aged 8–17 can join Kidpreneur!",
    "who is maav": "I am Maav, your friendly Kidpreneur AI agent. Ask me anything about the program!",
    "how do i choose a business idea": "Think about what you love, what problems you see, and what you can create or offer to help others.",
    "can i work with friends": "Yes! Teamwork is encouraged. You can start a business with friends or classmates.",
    "do i need money to start": "Many Kidpreneur projects can be started with little or no money. Creativity and effort matter most.",
    "how do i find customers": "Start by talking to family, friends, neighbors, and your community. Share your idea and ask for feedback.",
    "what is a prototype": "A prototype is a sample or early version of your product or service. It helps you test and improve your idea.",
    "how do i price my product": "Consider your costs, what customers are willing to pay, and what makes your product valuable.",
    "what is profit": "Profit is the money you make after paying for all your costs and expenses.",
    "how do i keep track of money": "Use a notebook, spreadsheet, or app to record your sales, costs, and profits.",
    "what if my idea fails": "Failure is part of learning. Review what happened, ask for feedback, and try again with new ideas.",
    "how do i advertise my business": "You can use posters, social media (with parent permission), word of mouth, and school events.",
    "can parents help": "Yes! Parents can guide, supervise, and help with safety, money, and planning.",
    "how do i ship products": "Package your products safely and use trusted delivery services. Ask parents for help with shipping.",
    "what is a mentor": "A mentor is someone with experience who gives advice, feedback, and encouragement.",
    "how do i get feedback": "Ask customers, friends, and family what they like and what could be better about your product.",
    "what is a launch": "A launch is when you officially start selling your product or service to customers.",
    "how do i set goals": "Write down what you want to achieve, break it into steps, and track your progress.",
    "can i sell online": "Yes, with parent permission. You can use kid-friendly marketplaces or your own website.",
    "what is marketing": "Marketing is how you tell people about your business and encourage them to buy.",
    "how do i handle competition": "Focus on what makes your business unique and always look for ways to improve.",
    "how do i stay safe": "Never share personal information online. Always ask parents before meeting customers or sharing details.",
    "what is customer service": "Customer service means helping your buyers, answering questions, and making sure they are happy.",
    "how do i reinvest profits": "Use some of your profits to buy more supplies, improve your product, or grow your business.",
    "can i change my idea": "Yes! You can always improve, pivot, or start a new project if you learn something new.",
    "how do i balance school and business": "Plan your time, set priorities, and make sure school comes first.",
    "what is a business plan": "A business plan is a simple document that explains your idea, goals, costs, and how you will succeed.",
    "how do i get inspiration": "Look for problems to solve, things you love, or ask Maav for ideas!",
    "can i sell services": "Yes! You can offer tutoring, pet care, tech help, or creative services.",
    "how do i make my business stand out": "Offer something unique, provide great service, and listen to your customers.",
    "what is branding": "Branding is how you design your business name, logo, and style to be memorable.",
    "how do i handle money": "Keep good records, ask parents for help, and save some of your earnings.",
    "can i get awards or recognition": "Kidpreneur offers badges, certificates, and celebrates your achievements!",
    "how do i join challenges": "Check the Kidpreneur dashboard for upcoming challenges and events.",
    "what is a cohort": "A cohort is a group of kids who start and learn together in the Kidpreneur program.",
    "how do i get started": "Sign up, pick an idea, and follow the roadmap. Maav is here to help!",
    "can i ask questions anytime": "Yes! Maav is always here to answer your Kidpreneur questions.",
    "how do i make my first sale": "Share your product, talk to potential customers, and offer great value.",
    "what is a pitch": "A pitch is a short explanation of your business idea to get interest or support.",
    "how do i improve my product": "Ask for feedback, test new ideas, and keep learning.",
    "can i get help with coding": "Kidpreneur teaches no-code tools, but you can ask for coding help if you want to learn more.",
    "how do i set prices": "Compare with similar products, consider your costs, and ask what customers are willing to pay.",
    "what is a marketplace": "A marketplace is a place where you can list and sell your products to buyers.",
    "how do i handle returns": "Be polite, listen to customer concerns, and offer solutions with parent guidance.",
    "can i make digital products": "Yes! You can create ebooks, art, games, or online courses.",
    "how do i get reviews": "Ask happy customers to share their feedback and testimonials.",
    "what is a streak": "A streak is a record of how many days you keep working or learning without stopping.",
    "how do i celebrate success": "Share your wins, earn badges, and thank your supporters!",
    "can i teach others": "Yes! You can offer tutoring, workshops, or share your skills with friends.",
    "how do i stay motivated": "Set small goals, celebrate progress, and ask Maav for encouragement!",
    "what is a prototype challenge": "A prototype challenge is a fun event to create and test new ideas quickly.",
    "how do i join mentor hours": "Check the dashboard for mentor hour schedules and sign up to get advice.",
    "can i get parent approval": "Always ask for parent approval before starting, selling, or sharing online.",
    "how do i track my progress": "Use the dashboard, set goals, and review your achievements regularly."
}

@app.route('/maav', methods=['POST'])
def maav():
    data = request.get_json()
    question = data.get('question', '').lower()
    # Find best match
    for key in KIDPRENEUR_FAQ:
        if key in question:
            return jsonify({"answer": KIDPRENEUR_FAQ[key]})
    return jsonify({"answer": "I'm Maav! Ask me anything about Kidpreneur and I'll help you out."})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
