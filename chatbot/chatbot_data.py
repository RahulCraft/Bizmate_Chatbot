# #chatbot_data.py

# chat_responses = {
#     "payroll": {
#         "response": "We offer automated payroll processing, salary disbursement, and compliance support.",
#         "link": "https://bizmate-hr.vercel.app/service/payroll"
#     },
#     "recruitment": {
#         "response": "Our recruitment solutions streamline candidate sourcing, screening, and hiring.",
#         "link": "https://bizmate-hr.vercel.app/service/recruitment"
#     },
#     "hrms": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/service/hrms"
#     },
#     "compliance": {
#         "response": "We help ensure labor law, tax, and industry regulation compliance.",
#         "link": "https://bizmate-hr.vercel.app/service/compliance"
#     },
#     "training": {
#         "response": "We provide employee training, onboarding programs, and skill development.",
#         "link": "https://bizmate-hr.vercel.app/service/training"
#     }
# }

# def get_bot_reply(user_msg):
#     msg = user_msg.lower()
#     for keyword, data in chat_responses.items():
#         if keyword in msg:
#             return f"{data['response']} Redirect here: {data['link']}"
#     return "Sorry, I couldn’t understand that. Please visit our homepage: https://bizmate-hr.vercel.app/"



# chatbot_data.py

# chat_responses = {
#     "payroll": {
#         "response": "We offer automated payroll processing, salary disbursement, and compliance support.",
#         "link": "https://bizmate-hr.vercel.app/service/payroll"
#     },
#     "recruitment": {
#         "response": "Our recruitment solutions streamline candidate sourcing, screening, and hiring.",
#         "link": "https://bizmate-hr.vercel.app/service/recruitment"
#     },
#     "hrms": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/service/hrms"
#     },
#     "compliance": {
#         "response": "We help ensure labor law, tax, and industry regulation compliance.",
#         "link": "https://bizmate-hr.vercel.app/service/compliance"
#     },
#     "training": {
#         "response": "We provide employee training, onboarding programs, and skill development.",
#         "link": "https://bizmate-hr.vercel.app/service/training"
#     },

#     # Greetings
#     "hi": {"response": "Hello! How can I assist you today?"},
#     "hello": {"response": "Hi there! Need any help?"},
#     "hey": {"response": "Hey! How can I help you?"},
#     "good morning": {"response": "Good morning! Hope you have a productive day!"},
#     "good afternoon": {"response": "Good afternoon! How can I assist you?"},
#     "good evening": {"response": "Good evening! What can I do for you?"},
#     "how are you": {"response": "I'm just a bot, but I'm functioning perfectly! How can I assist you?"},
#     "what can you do": {"response": "I can help you with your queries, just ask me something!"},
#     "who are you": {"response": "I'm your virtual assistant, here to help you out!"},
#     "help": {"response": "Sure, I'm here to help. Please tell me your question."},
#     "support": {"response": "You can ask your question here, and I'll do my best to assist you."},
#     "thanks": {"response": "You're welcome!"},
#     "thank you": {"response": "Glad I could help!"},
#     "bye": {"response": "Goodbye! Have a nice day!"},
#     "goodbye": {"response": "See you later! Stay safe!"},
#     "name": {"response": "Nice name! How can I assist you today?"},
#     "ok": {"response": "Alright! Feel free to ask more about our company or services."},
#     "okay": {"response": "Alright! Feel free to ask more about our company or services."}
# }

# def get_bot_reply(user_msg):
#     msg = user_msg.lower()
#     matched_keywords = []

#     for keyword in chat_responses.keys():
#         if keyword in msg:
#             matched_keywords.append(keyword)

#     if len(matched_keywords) == 1:
#         # Respond only with the specific service matched
#         key = matched_keywords[0]
#         data = chat_responses[key]
#         return f"{data['response']} Redirect here: {data['link']}"

#     elif len(matched_keywords) > 1:
#         # Respond with all services
#         reply = "Here’s a list of all our services:\n"
#         for key, data in chat_responses.items():
#             reply += f"- {key.capitalize()}: {data['response']} [More Info]({data['link']})\n"
#         return reply

#     else:
#         # No service matched
#         return "Sorry, I couldn’t understand that. Please visit our homepage: https://bizmate-hr.vercel.app/"

# Example usage:
# print(get_bot_reply("Tell me about payroll and training"))
# print(get_bot_reply("Do you offer HRMS?"))

# chatbot/chatbot_data.py

chat_responses = {
    # about  Bizmate HR Solution
    "bizmate_hr_solutions": {
    "response": "Bizmate HR Solutions is a purpose-driven HR consultancy led by Prashant Prem, an experienced HR leader and certified ICF-PCC coach. With over 30 years of leadership experience, Bizmate helps organizations grow sustainably by focusing on strategic HR, leadership development, and workplace transformation. We partner with businesses to build resilient, future-ready teams through tailored people-focused strategies.",
    "link": "https://bizmate-hr.vercel.app/about"
    },

    "bizmate": {
    "response": "Bizmate HR Solutions is a purpose-driven HR consultancy led by Prashant Prem, an experienced HR leader and certified ICF-PCC coach. With over 30 years of leadership experience, Bizmate helps organizations grow sustainably by focusing on strategic HR, leadership development, and workplace transformation. We partner with businesses to build resilient, future-ready teams through tailored people-focused strategies.",
    "link": "https://bizmate-hr.vercel.app/about"
    },

    "bizmate hr": {
    "response": "Bizmate HR Solutions is a purpose-driven HR consultancy led by Prashant Prem, an experienced HR leader and certified ICF-PCC coach. With over 30 years of leadership experience, Bizmate helps organizations grow sustainably by focusing on strategic HR, leadership development, and workplace transformation. We partner with businesses to build resilient, future-ready teams through tailored people-focused strategies.",   
    "link": "https://bizmate-hr.vercel.app/about"
    },

    "bizmate hr solutions": {
    "response": "Bizmate HR Solutions is a purpose-driven HR consultancy led by Prashant Prem, an experienced HR leader and certified ICF-PCC coach. With over 30 years of leadership experience, Bizmate helps organizations grow sustainably by focusing on strategic HR, leadership development, and workplace transformation. We partner with businesses to build resilient, future-ready teams through tailored people-focused strategies.",   
    "link": "https://bizmate-hr.vercel.app/about"
    },

    "bizmate hr solutions pvt ltd": {
    "response": "Bizmate HR Solutions is a purpose-driven HR consultancy led by Prashant Prem, an experienced HR leader and certified ICF-PCC coach. With over 30 years of leadership experience, Bizmate helps organizations grow sustainably by focusing on strategic HR, leadership development, and workplace transformation. We partner with businesses to build resilient, future-ready teams through tailored people-focused strategies.",   
    "link": "https://bizmate-hr.vercel.app/about"
    },

    # about  Bizmate HR Solution
    "company": {
    "response": "Our company, Bizmate HR Solutions, is a trusted HR consulting firm focused on people and performance. Led by experienced HR professional Prashant Prem, the company helps organizations grow by developing leadership, improving HR strategies, and transforming workplaces. With over 30 years of experience, our company supports sustainable growth for businesses through customized people-centric solutions.",
    "link": "https://bizmate-hr.vercel.app/about"
    },

    "organization": {
    "response": "Our company, Bizmate HR Solutions, is a trusted HR consulting firm focused on people and performance. Led by experienced HR professional Prashant Prem, the company helps organizations grow by developing leadership, improving HR strategies, and transforming workplaces. With over 30 years of experience, our company supports sustainable growth for businesses through customized people-centric solutions.",
    "link": "https://bizmate-hr.vercel.app/about"
    },

    "corpurate": {
    "response": "Our company, Bizmate HR Solutions, is a trusted HR consulting firm focused on people and performance. Led by experienced HR professional Prashant Prem, the company helps organizations grow by developing leadership, improving HR strategies, and transforming workplaces. With over 30 years of experience, our company supports sustainable growth for businesses through customized people-centric solutions.",
    "link": "https://bizmate-hr.vercel.app/about"
    },

    "business": {
    "response": "Our company, Bizmate HR Solutions, is a trusted HR consulting firm focused on people and performance. Led by experienced HR professional Prashant Prem, the company helps organizations grow by developing leadership, improving HR strategies, and transforming workplaces. With over 30 years of experience, our company supports sustainable growth for businesses through customized people-centric solutions.",   
    "link": "https://bizmate-hr.vercel.app/about"
    },

    # about  Bizmate HR Solution
    "experience": {
    "response": "Bizmate HR Solutions has years of strong experience in the recruitment industry. Our team has built deep expertise in connecting top talent with the right opportunities. From startups to large companies, we’ve helped organizations grow by delivering customized hiring solutions. Our success across industries reflects our commitment to excellence in recruitment and business growth.",
    "link": "https://bizmate-hr.vercel.app/"
    },


    #all services
    "all services": {
    "response": "We provide a complete suite of HR solutions tailored to your needs: 1. Strategic HR Advisory, 2. Leadership Development Programs, 3. Executive Coaching, 4. Recruitment, 5. Staffing Solutions, 6. Talent Management, 7. Culture & Engagement Consulting, 8. HSE Services, 9. Customized HR Solutions.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "services": {
    "response": "We provide a complete suite of HR solutions tailored to your needs: 1. Strategic HR Advisory, 2. Leadership Development Programs, 3. Executive Coaching, 4. Recruitment, 5. Staffing Solutions, 6. Talent Management, 7. Culture & Engagement Consulting, 8. HSE Services, 9. Customized HR Solutions.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "hr services": {
    "response": "We provide a complete suite of HR solutions tailored to your needs: 1. Strategic HR Advisory, 2. Leadership Development Programs, 3. Executive Coaching, 4. Recruitment, 5. Staffing Solutions, 6. Talent Management, 7. Culture & Engagement Consulting, 8. HSE Services, 9. Customized HR Solutions.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },


    # describe all services one by one
    "strategic hr advisory": {
    "response": "Our Strategic HR Advisory service helps businesses plan their human resources more effectively. We offer expert guidance on workforce planning, HR policy creation, and aligning HR with your company’s long-term goals.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "strategic hr advisory service": {
    "response": "Our Strategic HR Advisory service helps businesses plan their human resources more effectively. We offer expert guidance on workforce planning, HR policy creation, and aligning HR with your company’s long-term goals.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "strategic": {
    "response": "Our Strategic HR Advisory service helps businesses plan their human resources more effectively. We offer expert guidance on workforce planning, HR policy creation, and aligning HR with your company’s long-term goals.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },
    




    "leadership development": {
    "response": "We provide Leadership Development Programs to help your current and future leaders build strong management skills. These programs focus on decision-making, team building, communication, and emotional intelligence.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "leadership": {
    "response": "We provide Leadership Development Programs to help your current and future leaders build strong management skills. These programs focus on decision-making, team building, communication, and emotional intelligence.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "leadership development service": {
    "response": "We provide Leadership Development Programs to help your current and future leaders build strong management skills. These programs focus on decision-making, team building, communication, and emotional intelligence.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "leadership development program": {
    "response": "We provide Leadership Development Programs to help your current and future leaders build strong management skills. These programs focus on decision-making, team building, communication, and emotional intelligence.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },


    "executive coaching": {
    "response": "Our Executive Coaching service offers one-on-one guidance to top-level executives. It helps leaders improve personal performance, enhance leadership presence, and tackle business challenges effectively.",
    "link": "https://bizmate-hr.vercel.app/#services"
   },

    "executive coaching service": {
    "response": "Our Executive Coaching service offers one-on-one guidance to top-level executives. It helps leaders improve personal performance, enhance leadership presence, and tackle business challenges effectively.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "coaching": {
    "response": "Our Executive Coaching service offers one-on-one guidance to top-level executives. It helps leaders improve personal performance, enhance leadership presence, and tackle business challenges effectively.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },




   "recruitment solutions": {
   "response": "Our Recruitment Solutions help you find the right talent for your organization. We manage the entire hiring process – from screening to onboarding – so you can focus on growing your business.",
   "link": "https://bizmate-hr.vercel.app/#services"
   },

    "recruitment": {
    "response": "Our Recruitment Solutions help you find the right talent for your organization. We manage the entire hiring process – from screening to onboarding – so you can focus on growing your business.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "recruitment service": {
    "response": "Our Recruitment Solutions help you find the right talent for your organization. We manage the entire hiring process – from screening to onboarding – so you can focus on growing your business.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },



   "staffing solutions": {
   "response": "We offer flexible Staffing Solutions to meet your short-term and long-term workforce needs. Whether you need temporary staff or permanent employees, we help you build the right team quickly.",
   "link": "https://bizmate-hr.vercel.app/#services"
   },

    "staffing": {
    "response": "We offer flexible Staffing Solutions to meet your short-term and long-term workforce needs. Whether you need temporary staff or permanent employees, we help you build the right team quickly.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "staffing service": {
    "response": "We offer flexible Staffing Solutions to meet your short-term and long-term workforce needs. Whether you need temporary staff or permanent employees, we help you build the right team quickly.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },



   "talent management": {
   "response": "Our Talent Management services help you attract, develop, and retain top talent. We focus on employee development, career growth planning, and performance improvement.",
   "link": "https://bizmate-hr.vercel.app/#services"
   },

    "talent management service": {
    "response": "Our Talent Management services help you attract, develop, and retain top talent. We focus on employee development, career growth planning, and performance improvement.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "talent": {
    "response": "Our Talent Management services help you attract, develop, and retain top talent. We focus on employee development, career growth planning, and performance improvement.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },



   "culture engagement": {
   "response": "Our Culture & Engagement Consulting helps you build a positive and productive workplace. We work on improving employee engagement, workplace culture, and internal communication.",
   "link": "https://bizmate-hr.vercel.app/#services"
   },

    "culture engagement service": {
    "response": "Our Culture & Engagement Consulting helps you build a positive and productive workplace. We work on improving employee engagement, workplace culture, and internal communication.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "culture": {
    "response": "Our Culture & Engagement Consulting helps you build a positive and productive workplace. We work on improving employee engagement, workplace culture, and internal communication.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },



   "hse services": {
   "response": "Our HSE (Health, Safety, and Environment) services help you create a safe work environment. We assist in implementing safety policies, training employees, and ensuring legal compliance.",
   "link": "https://bizmate-hr.vercel.app/#services"
  },

    "hse": {
    "response": "Our HSE (Health, Safety, and Environment) services help you create a safe work environment. We assist in implementing safety policies, training employees, and ensuring legal compliance.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },
    "hse service": {
    "response": "Our HSE (Health, Safety, and Environment) services help you create a safe work environment. We assist in implementing safety policies, training employees, and ensuring legal compliance.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "health safety environment services": {
    "response": "Our HSE (Health, Safety, and Environment) services help you create a safe work environment. We assist in implementing safety policies, training employees, and ensuring legal compliance.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "health" :{
    "response": "Our HSE (Health, Safety, and Environment) services help you create a safe work environment. We assist in implementing safety policies, training employees, and ensuring legal compliance.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },
    "safety": {
    "response": "Our HSE (Health, Safety, and Environment) services help you create a safe work environment. We assist in implementing safety policies, training employees, and ensuring legal compliance.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },

    "environment": {
    "response": "Our HSE (Health, Safety, and Environment) services help you create a safe work environment. We assist in implementing safety policies, training employees, and ensuring legal compliance.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },



  "customized solutions": {
  "response": "We understand that every business is different. That’s why we offer Customized HR Solutions tailored to your unique challenges, goals, and workforce needs.",
  "link": "https://bizmate-hr.vercel.app/#services"
  },

    "customized hr solutions": {
    "response": "We understand that every business is different. That’s why we offer Customized HR Solutions tailored to your unique challenges, goals, and workforce needs.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },
    "customized hr service": {
    "response": "We understand that every business is different. That’s why we offer Customized HR Solutions tailored to your unique challenges, goals, and workforce needs.",
    "link": "https://bizmate-hr.vercel.app/#services"
    },











#    # Specific Services


#   "payroll": {
#         "response": "We offer automated payroll processing, salary disbursement, and compliance support.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },

#     "payroll management": {
#         "response": "We offer automated payroll processing, salary disbursement, and compliance support.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "payroll services": {
#         "response": "We offer automated payroll processing, salary disbursement, and compliance support.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "payroll software": {
#         "response": "We offer automated payroll processing, salary disbursement, and compliance support.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "payroll management system": {
#         "response": "We offer automated payroll processing, salary disbursement, and compliance support.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "payroll management software": {
#         "response": "We offer automated payroll processing, salary disbursement, and compliance support.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "payroll management system": {
#         "response": "We offer automated payroll processing, salary disbursement, and compliance support.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "payroll management software": {
#         "response": "We offer automated payroll processing, salary disbursement, and compliance support.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },



#     "recruitment": {
#         "response": "Our recruitment solutions streamline candidate sourcing, screening, and hiring.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "recruitment services": {
#         "response": "Our recruitment solutions streamline candidate sourcing, screening, and hiring.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "recruitment software": {
#         "response": "Our recruitment solutions streamline candidate sourcing, screening, and hiring.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "recruitment management system": {
#         "response": "Our recruitment solutions streamline candidate sourcing, screening, and hiring.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "recruitment management software": {
#         "response": "Our recruitment solutions streamline candidate sourcing, screening, and hiring.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "recruitment management": {
#         "response": "Our recruitment solutions streamline candidate sourcing, screening, and hiring.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },




#     "hrms": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "hr management system": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "hr software": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "hr management": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "human resource management system": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "human resource software": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "human resource management": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "employee management system": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "employee management software": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "employee management": {
#         "response": "Bizmate HRMS helps manage employee data, leaves, and attendance efficiently.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },


#     "compliance": {
#         "response": "We help ensure labor law, tax, and industry regulation compliance.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },
#     "compliance services": {
#         "response": "We help ensure labor law, tax, and industry regulation compliance.",
#         "link": "https://bizmate-hr.vercel.app/#services"
#     },





#     "training": {
#         "response": "We provide employee training, onboarding programs, and skill development.",
#         "link": "https://bizmate-hr.vercel.app"
#     },
#     "training services": {
#         "response": "We provide employee training, onboarding programs, and skill development.",
#         "link": "https://bizmate-hr.vercel.app"
#     },
#     "employee training": {
#         "response": "We provide employee training, onboarding programs, and skill development.",
#         "link": "https://bizmate-hr.vercel.app"
#     },
#     "employee onboarding": {
#         "response": "We provide employee training, onboarding programs, and skill development.",
#         "link": "https://bizmate-hr.vercel.app"
#     },
#     "skill development": {
#         "response": "We provide employee training, onboarding programs, and skill development.",
#         "link": "https://bizmate-hr.vercel.app"
#     },
#     "employee self service": {
#         "response": "We provide an employee self-service portal for managing personal information, leaves, and attendance.",
#         "link": "https://bizmate-hr.vercel.app/service/employee-self-service"
#     },
#     "employee self-service": {
#         "response": "We provide an employee self-service portal for managing personal information, leaves, and attendance.",
#         "link": "https://bizmate-hr.vercel.app/service/employee-self-service"
#     },
#     "employee self-service portal": {
#         "response": "We provide an employee self-service portal for managing personal information, leaves, and attendance.",
#         "link": "https://bizmate-hr.vercel.app/service/employee-self-service"
#     },




#     "attendance": {
#     "response": "We provide smart attendance and leave management systems with biometric and GPS tracking to help manage your workforce more effectively.",
#     "link": "https://bizmate-hr.vercel.app/service/attendance"
#     },
#     "attendance management": {
#     "response": "We provide smart attendance and leave management systems with biometric and GPS tracking to help manage your workforce more effectively.",
#     "link": "https://bizmate-hr.vercel.app/service/attendance"  
#     },
#     "leave": {
#     "response": "We provide smart attendance and leave management systems with biometric and GPS tracking to help manage your workforce more effectively.",
#     "link": "https://bizmate-hr.vercel.app/service/attendance"
#     },
#     "leave management": {
#     "response": "We provide smart attendance and leave management systems with biometric and GPS tracking to help manage your workforce more effectively.",
#     "link": "https://bizmate-hr.vercel.app/service/attendance"
#     },

    # Contact and Social Media
    "contact": {
    "response": "You can easily get in touch with us through the following ways:\n\n📧 Email: bizmatehr@gmail.com\n📞 Phone: +91-9289397570\n🌐 Website: https://bizmate-hr.vercel.app/\n\nWe’re happy to help you with any queries or HR solutions you need.",
    "link": "https://bizmate-hr.vercel.app/#contact"
     },

    "contact us": {
    "response": "You can easily get in touch with us through the following ways:\n\n📧 Email: bizmatehr@gmail.com\n📞 Phone: +91-9289397570\n🌐 Website: https://bizmate-hr.vercel.app/\n\nWe’re happy to help you with any queries or HR solutions you need.",
    "link": "https://bizmate-hr.vercel.app/#contact"
    },

    "get in touch": {
    "response": "You can easily get in touch with us through the following ways:\n\n📧 Email: bizmatehr@gmail.com\n📞 Phone: +91-9289397570\n🌐 Website: https://bizmate-hr.vercel.app/\n\nWe’re happy to help you with any queries or HR solutions you need.",
    "link": "https://bizmate-hr.vercel.app/#contact"
     },


     "call": {
    "response": "You can easily get in touch with us through the following ways:\n\n📧 Email: bizmatehr@gmail.com\n📞 Phone: +91-9289397570\n🌐 Website: https://bizmate-hr.vercel.app/\n\nWe’re happy to help you with any queries or HR solutions you need.",
    "link": "https://bizmate-hr.vercel.app/#contact"
     },

     "email": {
    "response": "You can easily get in touch with us through the following ways:\n\n📧 Email: bizmatehr@gmail.com\n📞 Phone: +91-9289397570\n🌐 Website: https://bizmate-hr.vercel.app/\n\nWe’re happy to help you with any queries or HR solutions you need.",
    "link": "https://bizmate-hr.vercel.app/#contact"
     },

      "touch": {
    "response": "You can easily get in touch with us through the following ways:\n\n📧 Email: bizmatehr@gmail.com\n📞 Phone: +91-9289397570\n🌐 Website: https://bizmate-hr.vercel.app/\n\nWe’re happy to help you with any queries or HR solutions you need.",
    "link": "https://bizmate-hr.vercel.app/#contact"
     },

      "calling": {
    "response": "You can easily get in touch with us through the following ways:\n\n📧 Email: bizmatehr@gmail.com\n📞 Phone: +91-9289397570\n🌐 Website: https://bizmate-hr.vercel.app/\n\nWe’re happy to help you with any queries or HR solutions you need.",
    "link": "https://bizmate-hr.vercel.app/#contact"
     },


     "contact": {
    "response": "You can easily get in touch with us through the following ways:\n\n📧 Email: bizmatehr@gmail.com\n📞 Phone: +91-9289397570\n🌐 Website: https://bizmate-hr.vercel.app/\n\nWe’re happy to help you with any queries or HR solutions you need.",
    "link": "https://bizmate-hr.vercel.app/#contact"
     },



    "connect": {
    "response": "You can contact us via email or phone for business inquiries or support. Visit our contact page for more details.",
    "link": "https://bizmate-hr.vercel.app/contact"
    },

    "social": {
    "response": "Follow us on our official social media pages to stay updated:\n\n- Instagram:https://www.instagram.com/bizmatehrofficial\n- LinkedIn: https://www.linkedin.com/company/bizmatehr\n- Facebook: https://www.facebook.com/bizmatehr\n- YouTube: https://www.youtube.com/@BizmateHR",
    "link": "https://bizmate-hr.vercel.app/"
    },

    "social media": {
    "response": "Follow us on our official social media pages to stay updated:\n\n- Instagram:https://www.instagram.com/bizmatehrofficial\n- LinkedIn: https://www.linkedin.com/company/bizmatehr\n- Facebook: https://www.facebook.com/bizmatehr\n- YouTube: https://www.youtube.com/@BizmateHR",
    "link": "https://bizmate-hr.vercel.app/"
    },

    "instagram": {
    "response": "Follow us on our official social media pages to stay updated:\n\n- Instagram:https://www.instagram.com/bizmatehrofficial\n- LinkedIn: https://www.linkedin.com/company/bizmatehr\n- Facebook: https://www.facebook.com/bizmatehr\n- YouTube: https://www.youtube.com/@BizmateHR",
    "link": "https://bizmate-hr.vercel.app/"
    },

    "fb": {
    "response": "Follow us on our official social media pages to stay updated:\n\n- Instagram:https://www.instagram.com/bizmatehrofficial/\n- LinkedIn: https://www.linkedin.com/company/bizmatehr\n- Facebook: https://www.facebook.com/bizmatehr\n- YouTube: https://www.youtube.com/@BizmateHR",
    "link": "https://bizmate-hr.vercel.app/"
    },

    "facebook": {
    "response": "Follow us on our official social media pages to stay updated:\n\n- Instagram:https://www.instagram.com/bizmatehrofficial/\n- LinkedIn: https://www.linkedin.com/company/bizmatehr\n- Facebook: https://www.facebook.com/bizmatehr\n- YouTube: https://www.youtube.com/@BizmateHR",
    "link": "https://bizmate-hr.vercel.app/"
    },

    "twitter": {
    "response": "Follow us on our official social media pages to stay updated:\n\n- Instagram:https://www.instagram.com/bizmatehrofficial/\n- LinkedIn: https://www.linkedin.com/company/bizmatehr\n- Facebook: https://www.facebook.com/bizmatehr\n- YouTube: https://www.youtube.com/@BizmateHR",
    "link": "https://bizmate-hr.vercel.app/"
    },

    "youtube": {
    "response": "Follow us on our official social media pages to stay updated:\n\n- Instagram:https://www.instagram.com/bizmatehrofficial/\n- LinkedIn: https://www.linkedin.com/company/bizmatehr\n- Facebook: https://www.facebook.com/bizmatehr\n- YouTube: https://www.youtube.com/@BizmateHR",
    "link": "https://bizmate-hr.vercel.app/"
    },

    "yt": {
    "response": "Follow us on our official social media pages to stay updated:\n\n- Instagram:https://www.instagram.com/bizmatehrofficial/\n- LinkedIn: https://www.linkedin.com/company/bizmatehr\n- Facebook: https://www.facebook.com/bizmatehr\n- YouTube: https://www.youtube.com/@BizmateHR",
    "link": "https://bizmate-hr.vercel.app/"
    },
    
    "linkedin": {
    "response": "Follow us on our official social media pages to stay updated:\n\n- Instagram:https://www.instagram.com/bizmatehrofficial/\n- LinkedIn: https://www.linkedin.com/company/bizmatehr\n- Facebook: https://www.facebook.com/bizmatehr\n- YouTube: https://www.youtube.com/@BizmateHR",
    "link": "https://bizmate-hr.vercel.app/"
    },


    "linkedin page": {
    "response": "Follow us on our official social media pages to stay updated:\n\n- Instagram:https://www.instagram.com/bizmatehrofficial/\n- LinkedIn: https://www.linkedin.com/company/bizmatehr\n- Facebook: https://www.facebook.com/bizmatehr\n- YouTube: https://www.youtube.com/@BizmateHR",
    "link": "https://bizmate-hr.vercel.app/"
    },


    # Greetings
    "hi": {"response": "Hello! How can I assist you today?"},
    "hello": {"response": "Hi there! Need any help?"},
    "hey": {"response": "Hey! How can I help you?"},
    "good morning": {"response": "Good morning! Hope you have a productive day!"},
    "good afternoon": {"response": "Good afternoon! How can I assist you?"},
    "good evening": {"response": "Good evening! What can I do for you?"},
    "how are you": {"response": "I'm just a bot, but I'm functioning perfectly! How can I assist you?"},
    "what can you do": {"response": "I can help you with your queries, just ask me something!"},
    "who are you": {"response": "I'm your virtual assistant, here to help you out!"},
    "help": {"response": "Sure, I'm here to help. Please tell me your question."},
    "support": {"response": "You can ask your question here, and I'll do my best to assist you."},
    "thanks": {"response": "You're welcome!"},
    "thank you": {"response": "Glad I could help!"},
    "bye": {"response": "Goodbye! Have a nice day!"},
    "goodbye": {"response": "See you later! Stay safe!"},
    "name": {"response": "Nice name! How can I assist you today?"},
    "ok": {"response": "Alright! Feel free to ask more about our company or services."},
    "okay": {"response": "Alright! Feel free to ask more about our company or services."}
}


def get_bot_reply(user_msg):
    msg = user_msg.lower()
    for keyword, data in chat_responses.items():
        if keyword in msg:
            # Check if it's a service with a link
            if "link" in data:
                return f"{data['response']} Redirect here: {data['link']}"
            else:
                return data["response"]
    return "Sorry, I couldn’t understand that. Please visit our homepage: https://bizmate-hr.vercel.app/"
