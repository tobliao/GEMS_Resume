from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    """Homepage for User/job seeker"""
    
    # about
    user = {
        "username": "Frank Liao",
        "firstname": "Frank",
        "lastname": "Liao"
    }
    summary = {
        "description": "An optimistic team player loves to share his domain know-how with members positively and patiently.",
    }
    # TODO: create variable and dictionary for contact info
    contact = {
        "phone": "(886)907781115",
        "email": "tobliao@cisco.com",
        "github": "https://github.com/tobliao",
        "linkedin": "https://www.linkedin.com/in/tobliao/",
        "address": "No. 460, Sec. 4, Xinyi Rd., Xinyi Dist., Taipei City."
    }

    # experience
    positions = [
        {
            "title": "ASIC Design Verification Engineer",
            "organization": "Cisco Systems Inc.",
            "description": "Full-time",
            "dates": "Jul 2022 – Present",
            "bullets": [
                "Designing UVM/SystemVerilog test benches.",
                "Enhancing existing test benches.",
                "End-to-end verification of various design blocks.",
                "Contributing to top-level verification.",
                "Be a part of emulation testing efforts and participate in the ASIC bring-up",
            ],
        },
        {
            "title": "IP Verification Engineer",
            "organization": "Siemens EDA",
            "dates": "Jul 2021 - Jul 2022 ",
            "description": "Full-time",
            "bullets": [
                "Take charge of I2C/I3C(HCI)/SMBus related product. (pure SystemVerilog/UVM-based project)",
                "   - Support customer’s integration issue on DUT slave/master without the language barriers/timezone issue. ",
                "   - Support customized requirement as the I2C/SMBus wrapped product also support the UVM integration. ",
                "   - Hold the training seminar on I2C/SMBus wrapper product for foreign customer and company’s colleague.",
                "Build up the UVM environment from scratch and establish an independent study group company-wise[1]: ",
                "   - Base on the familiar protocol, Ethernet, with the UVM and hold the study group biweekly.",
                "   - Build up the I2C and SMBus wrapped VIP with existing Avery proprietary product.(UVM-based)",
            ],
        },
        {
            "title": "Data Software Engineer (Infrastructure Development)",
            "organization": "Foxconn Industrial Internet",
            "dates": "2020.09 - 2021.7",
            "description": "Full-time",
            "bullets": [
                "Developed the main feature - Time Varied Scatter Plot. (Data Visualization/System Integration) ",
                "   - Integrated into the giant system within two months by Javascript",
                "   - Visualized the system information with D3J with senior backend engineers.",
                "Took charge of the Work Order System, micro-service, in python[2], including:",
                "   - Realtime data analytic and system integration and present with CI/CD process",
                "   - Data analysis and Machine Learning prediction and visualized with its own fullstack interface.",
            ],
        },
        {
            "title": "Contract Research Assistance",
            "organization": "Institute of Information Science, Academia Sinica",
            "dates": "2020.04 - 2020.08",
            "description": "Full-time",
            "bullets": [
                "“On Influencing the Influential: Disparity Seeding”, focusing on Graph Theory, Centrality Measurement",
                "Hands on experience of SDN environment setup with bare metal server and mininet for simulation, and led 2 master students with data-center debugging/trouble-shooting, leveraging some basic concepts on networking.",
            ],
        },   
    ]

    # education
    schools = [
        {
            "name": "The Hong Kong University of Science and Technology",
            "degree": "Master of Science",
            "major": "Electronic and Computer Engineering, Telecommunications",
            "desc": "Admission Scholarship. Data Analyst under Prof. K.S. WONG with self-build Machine Learning system.",
            "dur": "2019.08 - 2020.11"
        },
        {
            "name": "National Taiwan University of Science and Technology",
            "degree": "Bachelor of Science",
            "major": "Electrical Engineering",
            "desc": "Average GPA: 3.73/4.0, NTUST Outstanding Youth Awards (top 1%). Valedictorian of Graduation Ceremony.",
            "dur": "2014.09 - 2018.06"
        },
    ]
    

    return render_template(
        "index.html",
        # about
        title="Resume - Frank Liao",
        user=user,
        summary=summary,
        contact=contact,
        # experience
        positions=positions,
        # education
        schools=schools,
    )
    