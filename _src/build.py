#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build the static site for /home/wayne/mypage.

All content lives in this file. Edit the data below, run `python3 _src/build.py`,
and the HTML in the repo root is regenerated. Output is plain static HTML —
GitHub Pages needs no build step of its own.
"""
import os, html, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ------------------------------------------------------------------ profile --
ME = {
    "name":      "Wanyue Li",
    "name_cn":   "李皖越",
    "first":     "Wanyue",
    "last":      "Li",
    "role":      "Robotics Researcher",
    "email":     "liwy1024@connect.hku.hk",
    "location":  "Hong Kong",
    "github":    "https://github.com/liwanyue123",
    "programme": "Ph.D. Mechanical Engineering, HKU",
    "status":    "IROS 2025 Best RoboCup Paper Award",
}

# ---------------------------------------------------------------- education --
EDU = [
    ("2024.02 — present", "The University of Hong Kong",
     "Ph.D., Mechanical Engineering", "Hong Kong", "hku"),
    ("2020.09 — 2023.06", "Sun Yat-sen University",
     "M.S., Artificial Intelligence", "Guangzhou", "sysu"),
    ("2015.09 — 2019.06", "South China Agricultural University",
     "B.S., Computer Science and Technology", "Guangzhou", "scau"),
]

# --------------------------------------------------------------- experience --
EXPERIENCE = [
    ("2026.04 — present", "PNDbotics", "Robotics Algorithm Research Intern",
     "Developing dynamics-based interactive motion retargeting algorithms for humanoid robots."),
    ("2023.07 — 2024.02", "XPENG Robotics", "Motion Control Algorithm Developer",
     "Fully participated in the development of motion control algorithms for XPENG’s "
     "first-generation bipedal robot, PX5."),
]

# ------------------------------------------------------------------- honors --
HONORS = [
    ("2025.10", "IROS 2025", "Best RoboCup Paper Award", True),
    ("2025.08", "ATEC 2025 Tech Elite Competition", "5th Place", False),
    ("2023.08", "1st “Yat-sen Warrior Cup” Collaborative Robotics "
                "International Invitational", "Second Prize", False),
]

# ------------------------------------------------- systems & earlier work --
P = [
    {
        "slug": "xpeng-biped",
        "dir": "XPENG",
        "title": "XPENG Biped Robot",
        "year": "2023",
        "cat": "Bipedal Locomotion",
        "role": "Motion Control",
        "team": "XPENG Robotics",
        "tags": ["Dynamics", "Control", "Bionics"],
        "hero": "main",
        "hero_pos": "58% 42%",
        "blurb": "A 16-DoF biped that walks like a person — straight knees, low step frequency, strong disturbance resilience.",
        "lead": "Sixteen degrees of freedom, walking the way a person walks: straight knees, low step frequency, and enough disturbance resilience to keep going when it gets pushed.",
        "body": [
            ("Overview",
             ["We developed a 16-DoF bipedal robot capable of achieving human-like natural walking. The gait targets three things at once — <strong>straight knees</strong>, a <strong>low step frequency</strong>, and <strong>strong disturbance resilience</strong> — which together are what separate a machine that walks from a machine that merely does not fall over."]),
            ("My role",
             ["I was involved in the project from start to finish, working primarily on the development of <strong>motion control</strong>."]),
        ],
        "media": [
            {"type": "youtube", "id": "BNSZ8Fwcd20", "cap": "Walking trials"},
            {"type": "img", "src": "model", "cap": "Mechanical design", "mod": "media--tall"},
            {"type": "img", "src": "team", "cap": "The biped project team"},
        ],
    },
    {
        "slug": "bouncing-quadrotor",
        "dir": "Quadrotor",
        "title": "Bouncing Quadrotor",
        "year": "2023",
        "cat": "Aerial Robotics",
        "role": "Control system, end to end",
        "team": "RAPID Lab, Sun Yat-sen University",
        "tags": ["Dynamics", "Control", "Quadrotor"],
        "hero": "main",
        "hero_pos": "50% 38%",
        "blurb": "A quadrotor with a passive spring leg that travels by bouncing, for the energy it saves.",
        "lead": "A quadrotor that saves energy by refusing to stay in the air. A passive spring leg lets it advance in hops, with onboard sensing to find its way between them.",
        "body": [
            ("Overview",
             ["We developed a quadrotor with a <strong>passive spring</strong>, enabling energy-efficient jumping-flying rather than continuous powered flight. The robot carries a <strong>D435i</strong> depth camera and can autonomously navigate and evade obstacles."]),
            ("My role",
             ["I was responsible for developing the entire control system. The primary goal was to let the quadrotor accurately track its desired trajectory <strong>even after a significant impact with the ground</strong>.",
              "In the process I adapted and migrated the algorithm from the quadruped domain into the aerial one — feasible because both rest on the same foundation: a <strong>single rigid body model</strong>."]),
        ],
        "media": [
            {"type": "img", "src": "system", "cap": "System architecture"},
            {"type": "bilibili", "id": "aid=961550826&bvid=BV1SH4y1o71D&cid=1282078705&p=1&high_quality=1", "cap": "Jumping-flying trials"},
            {"type": "pair", "srcs": ["demo", "optitrack"], "caps": ["Bounce sequence", "Motion-capture arena"], "gif": ["demo"]},
        ],
    },
    {
        "slug": "slam-platform",
        "dir": "SLAM",
        "title": "SLAM Platform",
        "year": "2023",
        "cat": "State Estimation",
        "role": "Hardware & sensor drivers",
        "team": "with Peking University",
        "tags": ["Drivers", "Sensing", "GNSS"],
        "hero": "main",
        "hero_pos": "50% 55%",
        "blurb": "GNSS fused with fisheye and binocular vision, to hold position where satellites cannot be trusted.",
        "lead": "GNSS fails exactly where you need it most: between high-rises, under a car park. This platform pairs it with fisheye and binocular vision so the position survives the gap.",
        "body": [
            ("Overview",
             ["I collaborated with students from Peking University to develop a SLAM platform. The project addresses the degradation — or complete loss — of GNSS positioning accuracy caused by <strong>satellite signal blockage and multipath effects</strong> in urban high-rise areas and underground parking lots. Our answer is a positioning solution that fuses GNSS with <strong>fisheye and binocular cameras</strong>."]),
            ("My role",
             ["My work was centred on the hardware. I wrote the <strong>ROS drivers</strong> for the full sensor suite — fisheye cameras, depth cameras, GNSS, radar and lidar — and designed a <strong>circuit board capable of triggering every sensor synchronously</strong>."]),
        ],
        "media": [
            {"type": "pair", "srcs": ["mast", "lab"], "caps": ["Sensor mast", "Platform in the lab"]},
            {"type": "img", "src": "framework", "cap": "System overview"},
            {"type": "img", "src": "wiring", "cap": "Wiring and synchronous triggering"},
        ],
    },
    {
        "slug": "falling-cat-quadruped",
        "dir": "_disabled/FallingCat",
        "hidden": True,
        "title": "Falling-cat Quadruped",
        "year": "2023",
        "cat": "Bio-inspired Design",
        "role": "Lead, now advising",
        "team": "RAPID Lab, Sun Yat-sen University",
        "tags": ["Dynamics", "Control", "Bionics"],
        "hero": "fc-sq2",
        "hero_pos": "50% 45%",
        "blurb": "A spinal quadruped built to right itself in mid-air, the way a falling cat does.",
        "lead": "A cat with no angular momentum still lands on its feet. This robot is an attempt to do the same thing on purpose — bend the spine, flip, arrive upright.",
        "body": [
            ("Overview",
             ["The falling-cat problem inspires me, and I took on the development of a creative and difficult machine: a <strong>spinal quadruped robot that can flip in the air</strong>.",
              "To make that possible, not only the hardware and circuitry but also the <strong>motors are specially customised</strong> for this robot. On the algorithm side, the intent is to combine <strong>nonlinear MPC with deep reinforcement learning</strong>."]),
            ("My role",
             ["I began this project during my postgraduate years. Since I have already graduated, it has become the subject through which I guide the next generation of students."]),
        ],
        "media": [
            {"type": "pair", "srcs": ["fc-solidworks", "fc-rviz"], "caps": ["CAD assembly", "Simulation in RViz"]},
            {"type": "pair", "srcs": ["fc-fallingcat", "fc-isaac"], "caps": ["Aerial reorientation", "Isaac Gym training"], "gif": ["fc-fallingcat", "fc-isaac"]},
        ],
    },
    {
        "slug": "spined-quadruped",
        "dir": "SpinedQuadruped",
        "title": "Spined Quadruped Robot",
        "year": "2022",
        "cat": "Legged Locomotion",
        "role": "Everything but the structural design",
        "team": "RAPID Lab, Sun Yat-sen University",
        "tags": ["Dynamics", "Control", "Bionics", "ICRA 2023"],
        "hero": "main",
        "hero_pos": "50% 50%",
        "blurb": "Yat-sen Lion — a 15-DoF quadruped whose actuated spine is written into the MPC model.",
        "lead": "Most quadruped controllers treat the trunk as one rigid body. This one has a spine that moves, and an MPC formulation that knows it.",
        "body": [
            ("Overview",
             ["I developed a <strong>15-DoF quadruped robot with three actuated spine joints</strong>. The robot can freely change its spinal posture while trotting at high speed.",
              "The control contribution is a <strong>convex MPC approach that accounts for the movement of the spine</strong>, rather than modelling the trunk as a single rigid segment. The paper was accepted at ICRA 2023."]),
            ("My role",
             ["I took on the majority of the project tasks independently, with the exception of the structural design, which was handled by an engineer — hardware, electronics, control formulation, implementation and experiments."]),
        ],
                "links": [("Lab video on Bilibili", "https://www.bilibili.com/video/BV1Ed4y1M7Zy")],
        "media": [
            {"type": "youtube", "id": "BkEG_1_TQOw", "cap": "Trotting with active spine"},
            {"type": "pair", "srcs": ["cad", "assembly"], "caps": ["CAD assembly", "Build"]},
            {"type": "img", "src": "dofs", "cap": "Degrees of freedom"},
            {"type": "img", "src": "framework", "cap": "Control framework"},
            {"type": "img", "src": "notes", "cap": "Working notes", "mod": "media--tall"},
        ],
    },
    {
        "slug": "visual-inspection",
        "dir": "_disabled/VisualInspection",
        "hidden": True,
        "title": "Visual Inspection",
        "year": "2018",
        "cat": "Machine Vision",
        "role": "Sole developer",
        "team": "Industry commission",
        "tags": ["Computer Vision", "C#", "Halcon"],
        "hero": "vi-hero",
        "hero_pos": "50% 50%",
        "blurb": "Machine vision that catches grinding residue on pulley blanks and halts the line in real time.",
        "lead": "A grinder leaves residue on one part and every part after it is compromised. This device watches for the residue and tells the machine to stop.",
        "body": [
            ("Overview",
             ["When grinding pulley shapes by machine, residues are sometimes left behind — enough to significantly hinder the processing of every subsequent part. I developed a <strong>visual inspection device that uses morphology to detect such residues</strong> and then informs the machine to halt."]),
            ("My role",
             ["I received this project during my junior year and completed the entire development process independently, in <strong>C# and Halcon</strong> for their convenience in development.",]),
        ],
        "links": None,
        "media": [
            {"type": "youtube", "id": "Kyay1c6GN3w", "cap": "Detection running on the line"},
        ],
    },
]


# ----------------------------------------------------- research (HKU/ArcLab) --
# Papers from the doctorate. No photography yet — these render with a typographic
# "paper" tile instead of a hero image. Add "hero": "<asset-name>" to any of them
# once figures or footage exist, and it switches to the photographic layout.
R = [
    {
        "slug": "mgdp-depth-perception",
        "dir": "MGDP",
        "title": "MGDP — Generalized Depth Perception",
        "year": "2026",
        "cat": "Perceptive Locomotion",
        "role": "Co-author",
        "team": "ArcLab, HKU",
        "tags": ["Reinforcement Learning", "Perception", "Adv. Sci."],
        "hero": "cover",
        "hero_pos": "50% 45%",
        "tile": "Adv. Sci. 2026",
        "blurb": "A depth-perception model for quadruped locomotion that carries across nine different robots instead of being retrained for each one.",
        "lead": "Perception models for legged robots are usually welded to the robot they were trained on. MGDP separates the two, so the same perception front-end fine-tunes onto a new machine quickly.",
        "body": [
            ("Overview",
             ["MGDP is a perception-based deep reinforcement learning framework for quadruped locomotion. It uses a <strong>contrastive learning mechanism</strong> to extract highly generalized, low-dimensional terrain feature representations from multi-modal inputs — depth images and height maps — combined with an <strong>explicit depth-map denoising mechanism</strong>.",
              "Terrain-adaptive reward functions modulate penalty strength according to terrain characteristics, which lets the policy acquire complex locomotion skills — climbing, jumping, crawling, squeezing — in a <strong>single training stage, without distillation</strong>."]),
            ("Results",
             ["The pre-trained, dynamics-decoupled perception model fine-tunes quickly across quadruped morphologies. It was evaluated on <strong>nine distinct robots</strong> — A1, B1, Go1, Go2, Lite3, Spot, Aliengo, ANYmal C and Mini Cheetah — which despite large differences in dimensions and dynamics all traversed challenging terrain under the framework."]),
        ],
        "media": [
            {"type": "youtube", "id": "yOGQvbQMUKE", "cap": "Nine quadrupeds, one perception model"},
            {"type": "img", "src": "framework", "cap": "Framework"},
        ],
        "pub": {
            "authors": 'Yinzhao Dong, Ji Ma, Yidan Lu, Jiahui Zhang, <span class="me">Wanyue Li</span>, '
                       'Yeke Chen, Xuechao Chen, Zhangguo Yu, Peng Lu',
            "title": "MGDP: Mastering a Generalized Depth Perception Model for Quadruped Locomotion",
            "venue": "Advanced Science 2026",
            "state": "Published",
        },
        "links": [("Project page", "https://arclab-hku.github.io/MGDP/"),
                  ("Code on GitHub", "https://github.com/arclab-hku/MGDP"),
                  ("Wiley Online Library", "https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202524345")],
    },
    {
        "slug": "football-kicking",
        "dir": "Football",
        "title": "STOFT — Football Kicking",
        "year": "2025",
        "cat": "Bipedal Locomotion",
        "role": "First author",
        "team": "ArcLab, HKU",
        "tags": ["Trajectory Optimization", "Bipedal", "IROS 2025"],
        "hero": "main",
        "hero_pos": "50% 45%",
        "thumb": "image",
        "tile": "IROS 2025",
        "tile_mark": "Best RoboCup Paper",
        "blurb": "Spatial-temporal foot-trajectory optimization that lets a biped kick a ball where it aims — planned in under 1 ms, with a human-like backswing.",
        "lead": "Humanoid soccer asks a robot to stay stable through an aggressive motion and still put the ball exactly where it intended. This work takes spatial-temporal trajectory planning out of drone research and hands it to a leg.",
        "body": [
            ("The problem",
             ["Humanoid robot soccer presents two difficulties at once: <strong>maintaining system stability during aggressive kicking motions</strong> while <strong>achieving precise ball trajectory control</strong>. Existing solutions — traditional position-based control and reinforcement learning alike — show significant limitations.",
              "Model predictive control is the prevalent approach for ordinary quadruped and biped robots, and it has clear advantages. But existing studies tend to oversimplify the leg swing, relying merely on simple trajectory interpolation. That severely constrains the foot’s ability to interact with its environment, and hinders tasks such as ball kicking."]),
            ("Approach",
             ["This study adapts the <strong>spatial-temporal trajectory planning</strong> method — successful in drone applications — to bipedal robotic systems. The approach autonomously generates foot trajectories that satisfy constraints on <strong>target kicking position, velocity and acceleration</strong>, while simultaneously <strong>optimizing the duration of the swing phase</strong>."]),
            ("Results",
             ["The optimized trajectories closely mimic human kicking behaviour, including a <strong>backswing motion</strong>. Simulation and hardware experiments confirm the algorithm’s efficiency and reliability: <strong>trajectory planning in under 1 ms</strong>, and <strong>nearly 100 % task completion accuracy</strong> when the soccer goal lies within −90° to 90°."]),
        ],
        "pub": {
            "authors": '<span class="me">Wanyue Li</span>, Ji Ma, Minghao Lu, Peng Lu*',
            "title": "Like Playing a Video Game: Spatial-Temporal Optimization of Foot Trajectories for Controlled Football Kicking in Bipedal Robots",
            "venue": "IEEE/RSJ IROS 2025",
            "state": "Best RoboCup Paper Award",
        },
        "media": [
            {"type": "youtube", "id": "g-LRctlbztE", "cap": "Kicking trials in simulation and hardware"},
            {"type": "img", "src": "teaser", "cap": "STOFT — aiming, foot orientation, trajectory optimization, adaptive gait, precision shooting", "mod": "media--tall"},
            {"type": "img", "src": "certificate", "cap": "IROS 2025 Best RoboCup Paper Award"},
        ],
        "links": [("arXiv:2510.01843", "https://arxiv.org/abs/2510.01843"),
                  ("IEEE Xplore", "https://ieeexplore.ieee.org/document/11246655/"),
                  ("Demo video", "https://www.youtube.com/watch?v=g-LRctlbztE")],
    },
    {
        "slug": "mild-deformable-terrain",
        "dir": "MILD",
        "title": "MILD — Walking on Ground That Yields",
        "year": "2025",
        "cat": "Bipedal Locomotion",
        "role": "Co-author",
        "team": "ArcLab, HKU",
        "tags": ["Simulation", "Reinforcement Learning", "IEEE RA-L"],
        "hero": "main",
        "hero_pos": "50% 50%",
        "thumb": "image",
        "tile": "IEEE RA-L 2025",
        "blurb": "A physics-grounded contact solver that makes yielding terrain tractable to simulate, plus a terrain-aware controller trained on it.",
        "lead": "Sand, mud, snow. Bipeds struggle on ground that gives way, largely because the simulators they are trained in do not model it. MILD starts there.",
        "body": [
            ("Overview",
             ["Enabling robots to walk on yielding terrain matters for everything from disaster response to planetary exploration. Bipedal robots hold real potential there, but their locomotion on deformable surfaces remains limited — current simulators fail to capture the <strong>spatiotemporal heterogeneity</strong> of such yielding substrates.",
              "MILD introduces a <strong>physics-grounded discrete-element contact solver</strong> that accurately simulates spatially varying foot–terrain interactions. Alongside it, a <strong>terrain-aware locomotion controller</strong> is trained via deep reinforcement learning with latent modulation and proprioceptive estimation."]),
            ("Results",
             ["Quantitative comparison against state-of-the-art methods shows the approach generates more diverse and more realistic contact scenarios."]),
        ],
        "pub": {
            "authors": 'Zeren Luo, Jiahui Zhang, Zhe Xu, <span class="me">Wanyue Li</span>, Xinqi Li, Xuechao Chen, Zhangguo Yu, Annan Tang, Peng Lu*',
            "title": "MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces",
            "venue": "IEEE Robotics and Automation Letters (RA-L 2025)",
            "state": "Published",
        },
        "links": [("IEEE Xplore", "https://ieeexplore.ieee.org/document/11302803"),
                  ("Demo video", "https://www.youtube.com/watch?v=80Zg2vUkM7A")],
        "media": [
            {"type": "youtube", "id": "80Zg2vUkM7A", "cap": "Walking on deformable ground"},
            {"type": "img", "src": "main",
             "cap": "Discrete-element contact model — granular substrates, friction cone, drag on the bottom surface"},
        ],
    },
    {
        "slug": "marg-gap-terrain",
        "dir": "MARG",
        "title": "MARG — Risky Gap Terrains",
        "year": "2025",
        "cat": "Perceptive Locomotion",
        "role": "Co-author",
        "team": "ArcLab, HKU",
        "tags": ["Reinforcement Learning", "Elevation Mapping", "IEEE T-RO"],
        "hero": "terrains",
        "hero_pos": "50% 50%",
        "tile": "IEEE T-RO 2025",
        "blurb": "Elevation maps fused with proprioception so a legged robot can pick footholds across gaps — with the map built from a single LiDAR.",
        "lead": "Blind locomotion controllers fall into holes. MARG gives the policy a terrain map and asks it to choose where to put its feet.",
        "body": [
            ("Overview",
             ["Existing blind locomotion controllers often struggle to ensure safe, efficient traversal of <strong>risky gap terrains</strong>, which are highly complex and require the robot to perceive terrain accurately and select appropriate footholds while moving.",
              "MARG is a deep reinforcement learning controller that <strong>integrates terrain maps with proprioception</strong> to dynamically adjust its action and improve stability. Its terrain mapping model (TMG) relies on a <strong>single LiDAR</strong> to generate accurate terrain maps, which keeps hardware deployment simple."]),
            ("Results",
             ["Experiments show the MARG controller is stable and effective across risky tasks, balancing safety, stability and efficiency during locomotion."]),
        ],
        "pub": {
            "authors": 'Yinzhao Dong, Ji Ma, Liu Zhao, <span class="me">Wanyue Li</span>, Peng Lu*',
            "title": "MARG: MAstering Risky Gap Terrains for Legged Robots with Elevation Mapping",
            "venue": "IEEE Transactions on Robotics (T-RO 2025), 41:6123–6139",
            "state": "Published",
        },
        "media": [
            {"type": "youtube", "id": "cVeQD845ER0", "cap": "Crossing risky gap terrain"},
        ],
        "links": [("Project page", "https://astrorix.github.io/MARG/"),
                  ("arXiv:2509.20036", "https://arxiv.org/abs/2509.20036"),
                  ("IEEE Xplore", "https://ieeexplore.ieee.org/document/11196002")],
    },
    {
        "slug": "rm-planner",
        "dir": "RM_planner",
        "title": "RM-Planner — Mobile Manipulation",
        "year": "2025",
        "cat": "Manipulation",
        "role": "Co-author",
        "team": "Sun Yat-sen University · HKU",
        "tags": ["Reinforcement Learning", "Whole-body MPC", "ICRA 2025"],
        "hero": "main",
        "hero_pos": "50% 45%",
        "tile": "ICRA 2025",
        "blurb": "A two-layer planner: an RL policy reads raw 3D point clouds to choose manipulation postures, a whole-body MPC layer tracks them safely.",
        "lead": "Mobile manipulation in an unknown environment splits badly into “where to stand” and “how to move”. RM-Planner puts learning on the first and model-based control on the second.",
        "body": [
            ("Overview",
             ["RM-Planner is a planning method for mobile manipulation in unknown, complex environments. It adopts a <strong>two-layer hierarchical framework</strong>.",
              "The low-level planner is a <strong>whole-body MPC</strong> that tracks subgoals and generates aggressive but safe joint commands across the whole manipulation process. The high-level policy is <strong>reinforcement-learned and consumes 3D point-cloud representations of the environment directly</strong>, guiding the robot toward optimal manipulation postures given current observations and the task objective."]),
            ("Results",
             ["RM-Planner significantly outperforms state-of-the-art methods in extensive simulation and real-world experiments."]),
        ],
        "pub": {
            "authors": 'Zixuan Zhuang, Le Zheng, <span class="me">Wanyue Li</span>, Renming Liu, Peng Lu, Hui Cheng*',
            "title": "RM-Planner: Integrating Reinforcement Learning with Whole-Body Model Predictive Control for Mobile Manipulation",
            "venue": "IEEE ICRA 2025",
            "state": "Published",
        },
        "links": [("IEEE Xplore", "https://ieeexplore.ieee.org/document/11127719"),
                  ("Demo video", "https://www.bilibili.com/video/BV1atQ6YqEdm/")],
        "media": [
            {"type": "bilibili", "id": "bvid=BV1atQ6YqEdm&p=1&high_quality=1",
             "cap": "Mobile manipulation trials"},
        ],
    },
]

# projects flagged "hidden" drop out of the lists, the generated pages,
# prev/next navigation and the sitemap. Flip the flag to bring one back.
R = [p for p in R if not p.get("hidden")]
P = [p for p in P if not p.get("hidden")]
ALL = R + P

# ------------------------------------------------------------- publications --
PUBS = [
    {
        "authors": 'Yinzhao Dong, Ji Ma, Yidan Lu, Jiahui Zhang, <span class="me">Wanyue Li</span>, '
                   'Yeke Chen, Xuechao Chen, Zhangguo Yu, Peng Lu',
        "title": "MGDP: Mastering a Generalized Depth Perception Model for Quadruped Locomotion",
        "venue": "Adv. Sci. 2026", "year": "2026", "award": None, "slug": "mgdp-depth-perception",
    },
    {
        "authors": 'Ji Ma, Yinzhao Dong, <span class="me">Wanyue Li</span>, Peng Lu*',
        "title": "MASH: MAstering Safe and High-Speed Quadruped Navigation with Adaptive Gait Transitions",
        "venue": "IEEE T-FR 2026", "year": "2026", "award": None, "slug": None,
    },
    {
        "authors": '<span class="me">Wanyue Li</span>, Ji Ma, Minghao Lu, Peng Lu*',
        "title": "Like Playing a Video Game: Spatial-Temporal Optimization of Foot "
                 "Trajectories for Controlled Football Kicking in Bipedal Robots",
        "venue": "IROS 2025", "year": "2025", "award": "Best RoboCup Paper Award", "slug": "football-kicking",
    },
    {
        "authors": 'Zeren Luo, Jiahui Zhang, Zhe Xu, <span class="me">Wanyue Li</span>, '
                   'Xinqi Li, Xuechao Chen, Zhangguo Yu, Annan Tang, Peng Lu*',
        "title": "MILD: Tractable Terrain Modeling for Learning Improved Bipedal "
                 "Locomotion on Deformable Surfaces",
        "venue": "IEEE RA-L 2025", "year": "2025", "award": None, "slug": "mild-deformable-terrain",
    },
    {
        "authors": 'Yinzhao Dong, Ji Ma, Liu Zhao, <span class="me">Wanyue Li</span>, Peng Lu*',
        "title": "MARG: MAstering Risky Gap Terrains for Legged Robots with Elevation Mapping",
        "venue": "IEEE T-RO 2025", "year": "2025", "award": None, "slug": "marg-gap-terrain",
    },
    {
        "authors": 'Zixuan Zhuang, Le Zheng, <span class="me">Wanyue Li</span>, '
                   'Renming Liu, Peng Lu, Hui Cheng*',
        "title": "RM-Planner: Integrating Reinforcement Learning with Whole-Body Model "
                 "Predictive Control for Mobile Manipulation",
        "venue": "ICRA 2025", "year": "2025", "award": None, "slug": "rm-planner",
    },
    {
        "authors": '<span class="me">Wanyue Li</span>, Zida Zhou, Hui Cheng*',
        "title": "Dynamic Locomotion of a Quadruped Robot with Active Spine via "
                 "Model Predictive Control",
        "venue": "ICRA 2023", "year": "2023", "award": None, "slug": "spined-quadruped",
    },
]

SKILLS = [
    ("Algorithms", ["Imitation Learning", "Reinforcement Learning", "Motion Retargeting",
                    "Model Predictive Control", "Trajectory Optimization"]),
    ("Frameworks", ["ROS / ROS2", "Isaac Lab / Isaac Gym", "MuJoCo", "Pinocchio", "CasADi"]),
    ("Programming", ["C / C++", "Python", "MATLAB"]),
]

GALLERY = [
    ("Beyond/model-study", "3D model study"),
    ("Beyond/painting", "Painting"),
    ("Beyond/modelling", "Modelling in progress"),
    ("Beyond/graffiti", "Graffiti"),
    ("Beyond/render", "Render"),
    ("Beyond/furnace1", "Iron-smelting furnace"),
    ("Beyond/whiteboard", "Whiteboard"),
    ("Beyond/furnace2", "Furnace, in build"),
    ("Beyond/furnace3", "Furnace, fired"),
]

# --------------------------------------------------------------- templating --
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Inter+Tight:wght@400;500;600&family=JetBrains+Mono:wght@400;500'
         '&family=Instrument+Serif:ital@0;1&display=swap">')

def head(title, desc, extra=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="author" content="{ME['name']}">
<meta name="theme-color" content="#0A0A0B">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{ME['name']}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/favicon.svg">
{FONTS}
<link rel="stylesheet" href="/assets/css/main.css">
{extra}
</head>
<body>"""

def nav(active=""):
    def L(href, label, spy=None, hide=False):
        cls = "nav__link" + (" nav__link--hide-sm" if hide else "")
        if active and active == label.lower():
            cls += " is-active"
        sp = f' data-spy="{spy}"' if spy else ""
        return f'<a class="{cls}" href="{href}"{sp}>{label}</a>'
    return f"""<nav class="nav">
  <a class="nav__brand" href="/"><span class="nav__mark" aria-hidden="true"></span>{ME['name']}</a>
  <div class="nav__links">
    {L('/#work', 'Work', 'work')}
    {L('/#publications', 'Publications', 'publications', hide=True)}
    {L('/#about', 'About', 'about')}
    {L('/beyond/', 'Beyond', hide=True)}
    <a class="nav__link" href="/assets/cv/wanyue-li-cv-en.pdf">CV</a>
  </div>
</nav>"""

def footer():
    return f"""<footer class="footer wrap">
  <span>&copy; <span data-year>2026</span> {ME['name']}</span>
  <span>{ME['location']}</span>
  <a href="{ME['github']}" rel="noopener">GitHub &nearr;</a>
</footer>
<script src="/assets/js/main.js" defer></script>
</body>
</html>"""

def picture(name, alt, sizes="100vw", cls="", loading="lazy", pos=None):
    """Responsive <img> for an optimised asset (sm/md/lg jpgs), or a gif as-is.

    `name` is a path relative to assets/img without extension, e.g. "MGDP/main".
    """
    style = f' style="object-position:{pos}"' if pos else ""
    if os.path.exists(os.path.join(ROOT, "assets", "img", name + ".gif")):
        return (f'<img src="/assets/img/{name}.gif" alt="{html.escape(alt)}" '
                f'class="{cls}" loading="{loading}" decoding="async"{style}>')
    return (f'<img src="/assets/img/{name}-md.jpg" '
            f'srcset="/assets/img/{name}-sm.jpg 640w, /assets/img/{name}-md.jpg 1100w, /assets/img/{name}-lg.jpg 1800w" '
            f'sizes="{sizes}" alt="{html.escape(alt)}" class="{cls}" '
            f'loading="{loading}" decoding="async"{style}>')

def resolve(src, base):
    """Bare names are relative to the project's image folder."""
    return src if "/" in src or not base else f"{base}/{src}"


def media_block(m, base=""):
    if m["type"] == "youtube":
        return (f'<figure class="media"><div class="embed"><iframe '
                f'src="https://www.youtube-nocookie.com/embed/{m["id"]}" '
                f'title="{html.escape(m["cap"])}" loading="lazy" '
                f'allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" '
                f'allowfullscreen></iframe></div>'
                f'<figcaption>{html.escape(m["cap"])}</figcaption></figure>')
    if m["type"] == "bilibili":
        return (f'<figure class="media"><div class="embed"><iframe '
                f'src="https://player.bilibili.com/player.html?{m["id"]}" '
                f'title="{html.escape(m["cap"])}" loading="lazy" scrolling="no" '
                f'frameborder="0" allowfullscreen></iframe></div>'
                f'<figcaption>{html.escape(m["cap"])}</figcaption></figure>')
    if m["type"] == "pair":
        gif = set(m.get("gif", []))
        cells = "".join(
            f'<figure>{picture(resolve(s, base), c, "(max-width:900px) 100vw, 45vw")}'
            f'<figcaption>{html.escape(c)}</figcaption></figure>'
            for s, c in zip(m["srcs"], m["caps"]))
        return f'<div class="media media--pair">{cells}</div>'
    mod = m.get("mod", "")
    return (f'<figure class="media {mod}">'
            f'{picture(resolve(m["src"], base), m["cap"], "(max-width:900px) 100vw, 68vw")}'
            f'<figcaption>{html.escape(m["cap"])}</figcaption></figure>')

# -------------------------------------------------------------------- index --
SIG_TAGS = ("ICRA", "IROS", "IEEE", "Adv. Sci.", "T-RO", "T-FR", "RA-L")

def work_row(p, i):
    """One row of the Selected work list. Falls back to a typographic tile when
    the project has no photography yet."""
    tags = "".join(
        f'<span class="tag{" tag--sig" if t.startswith(SIG_TAGS) else ""}">{html.escape(t)}</span>'
        for t in p["tags"])
    if p.get("hero"):
        thumb = ('<span class="work-row__thumb">'
                 + picture(resolve(p.get("thumb") or "main", p["dir"]), p["title"],
                           "(max-width:860px) 100vw, (max-width:1180px) 220px, 300px")
                 + "</span>")
    else:
        mark = (f'<span class="paper-tile__mark">{html.escape(p["tile_mark"])}</span>'
                if p.get("tile_mark") else "")
        thumb = ('<span class="work-row__thumb work-row__thumb--paper">'
                 f'<span class="paper-tile__venue">{html.escape(p.get("tile", p["year"]))}</span>'
                 f'{mark}</span>')
    return f"""<a class="work-row reveal" href="/work/{p['slug']}/" style="--d:{i*45}ms">
  <span class="work-row__idx">{i:02d}</span>
  {thumb}
  <span class="work-row__body">
    <span class="work-row__title">{html.escape(p['title'])}</span>
    <span class="work-row__sub">{p['blurb']}</span>
    <span class="work-row__tags">{tags}</span>
  </span>
  <span class="work-row__aside">
    <span>{p['year']}</span>
    <span class="work-row__arrow" aria-hidden="true">
      <svg width="13" height="13" viewBox="0 0 13 13" fill="none" stroke="currentColor" stroke-width="1.4">
        <path d="M1 12L12 1M12 1H3.5M12 1v8.5"/></svg>
    </span>
  </span>
</a>"""


def build_index():
    research = "".join(work_row(p, i) for i, p in enumerate(R, 1))
    earlier  = "".join(work_row(p, i) for i, p in enumerate(P, len(R) + 1))

    pubs = []
    for i, b in enumerate(PUBS, 1):
        award = (f'<span class="chip chip--accepted">{html.escape(b["award"])}</span>'
                 if b.get("award") else "")
        title = html.escape(b["title"])
        if b.get("slug"):
            title = f'<a href="/work/{b["slug"]}/">{title}</a>'
        pubs.append(f"""<article class="pub reveal" style="--d:{i*45}ms">
  <span class="pub__idx">[{i}]</span>
  <div>
    <h3 class="pub__title">{title}</h3>
    <p class="pub__authors">{b['authors']}</p>
    <p class="pub__venue"><span class="chip">{html.escape(b['venue'])}</span>{award}</p>
  </div>
  <span class="pub__year">{b['year']}</span>
</article>""")

    exp = "".join(f"""<div class="tl reveal" style="--d:{i*50}ms">
  <span class="tl__when">{html.escape(when)}</span>
  <div class="tl__body">
    <h4 class="tl__what">{html.escape(org)}</h4>
    <p class="tl__role">{html.escape(role)}</p>
    <p class="tl__note">{html.escape(note)}</p>
  </div>
</div>""" for i, (when, org, role, note) in enumerate(EXPERIENCE, 1))

    edu = "".join(f"""<div class="tl tl--edu reveal" style="--d:{i*50}ms">
  <span class="tl__when">{html.escape(when)}</span>
  <div class="tl__body">
    <img class="tl__logo" src="/assets/img/school/{logo}.png" alt="" width="48" height="48" loading="lazy">
    <div>
      <h4 class="tl__what">{html.escape(org)}</h4>
      <p class="tl__role">{html.escape(deg)}</p>
    </div>
  </div>
  <span class="tl__where">{html.escape(place)}</span>
</div>""" for i, (when, org, deg, place, logo) in enumerate(EDU, 1))

    honors = "".join(f"""<div class="tl tl--honor reveal" style="--d:{i*50}ms">
  <span class="tl__when">{html.escape(when)}</span>
  <div class="tl__body">
    <h4 class="tl__what">{html.escape(what)}</h4>
  </div>
  <span class="chip{' chip--accepted' if star else ''}">{html.escape(prize)}</span>
</div>""" for i, (when, what, prize, star) in enumerate(HONORS, 1))

    skills = "".join(
        f'<div class="skills__group"><h3>{html.escape(g)}</h3><div class="skills__items">'
        + "".join(f"<span>{html.escape(x)}</span>" for x in items)
        + "</div></div>" for g, items in SKILLS)

    hero_img = picture("XPENG/main", "", "100vw", loading="eager", pos="58% 42%")

    doc = head(
        f"{ME['name']} — Robotics Researcher",
        "Wanyue Li is a Ph.D. student in Mechanical Engineering at the University of Hong Kong, "
        "working on legged robots — bipedal locomotion, model predictive control and learning.",
    ) + nav() + f"""
<main>

<header class="hero">
  <div class="hero__bg" aria-hidden="true">{hero_img}</div>
  <div class="hero__inner wrap">
    <p class="eyebrow reveal">Robotics &middot; Legged Locomotion &middot; Control &amp; Learning</p>
    <h1 class="hero__name">
      <span class="line-mask"><span style="--d:80ms">{ME['first']}</span></span>
      <span class="line-mask"><span class="t2" style="--d:200ms">{ME['last']}</span></span>
    </h1>
    <div class="hero__grid">
      <p class="lead reveal" style="--d:340ms">
        I've built hardware platforms for <strong>wheeled robots</strong>, <strong>drones</strong>,
        <strong>quadrupeds</strong>, and <strong>humanoids</strong>, and I specialize in
        <strong>optimization-based</strong> and <strong>RL-based</strong> motion control.
        <span class="serif-em">Lately I've been researching motion generation.</span>
      </p>
      <dl class="hero__meta reveal" style="--d:440ms">
        <div><dt>Based</dt><dd>{ME['location']}</dd></div>
        <div><dt>Doctorate</dt><dd>{ME['programme']}</dd></div>
        <div><dt>Recent</dt><dd><span class="sig">&bull;</span> {ME['status']}</dd></div>
      </dl>
    </div>
    <a class="scroll-cue reveal" href="#work" style="--d:560ms"><i aria-hidden="true"></i>Selected work</a>
  </div>
</header>

<section class="section" id="work">
  <div class="wrap">
    <div class="section__head reveal">
      <h2 class="section__title">Selected work</h2>
      <p class="eyebrow">{len(ALL):02d} projects &middot; {min(p["year"] for p in ALL)}&ndash;{max(p["year"] for p in ALL)}</p>
    </div>

    <p class="group-label reveal">Doctoral research &mdash; ArcLab, HKU &middot; 2024&ndash;present</p>
    <div class="work-list">{research}</div>

    <p class="group-label group-label--gap reveal">Earlier work &middot; {min(p["year"] for p in P)}&ndash;{max(p["year"] for p in P)}</p>
    <div class="work-list">{earlier}</div>
  </div>
</section>

<section class="section" id="publications">
  <div class="wrap">
    <div class="section__head reveal">
      <h2 class="section__title">Publications</h2>
      <p class="eyebrow">{len(PUBS):02d} papers &middot; * corresponding</p>
    </div>
    {"".join(pubs)}
  </div>
</section>

<section class="section" id="record">
  <div class="wrap">
    <div class="section__head reveal">
      <h2 class="section__title">Experience</h2>
      <p class="eyebrow">Industry</p>
    </div>
    <div class="tl-list">{exp}</div>

    <div class="section__head reveal" style="margin-top:clamp(3.5rem,7vw,6rem)">
      <h2 class="section__title">Education</h2>
      <p class="eyebrow">2015 &ndash; present</p>
    </div>
    <div class="tl-list">{edu}</div>

    <div class="section__head reveal" style="margin-top:clamp(3.5rem,7vw,6rem)">
      <h2 class="section__title">Honors</h2>
      <p class="eyebrow">Awards &amp; competitions</p>
    </div>
    <div class="tl-list">{honors}</div>
  </div>
</section>

<section class="section" id="about">
  <div class="wrap">
    <div class="section__head reveal">
      <h2 class="section__title">About</h2>
      <p class="eyebrow">{ME['name_cn']}</p>
    </div>
    <div class="about">
      <div class="about__body reveal">
        <p class="lead">
          I am a <strong>Ph.D. student in Mechanical Engineering at the University of Hong Kong</strong>,
          working on legged robots &mdash; bipeds above all. Before that I took an M.S. in Artificial
          Intelligence at Sun Yat-sen University, and spent seven months at <strong>XPENG Robotics</strong>
          on the motion control for PX5, their first-generation biped.
        </p>
        <p class="lead" style="margin-top:1.5rem">
          What ties the work together is the dynamics. A quadruped with an actuated spine and a quadrotor
          with a spring leg look nothing alike, but both reduce to a single rigid body in contact with the
          world &mdash; which is why the MPC formulation written for one transferred to the other almost intact.
        </p>
        <p class="lead" style="margin-top:1.5rem">
          These days the work leans on both halves at once: trajectory optimization and whole-body MPC on the
          model side, imitation and reinforcement learning on the other.
          <span class="serif-em">Most of the interesting problems live where the two meet.</span>
        </p>
        <div class="skills">{skills}</div>
      </div>
      <figure class="about__figure reveal" style="--d:120ms">
        {picture("SpinedQuadruped/assembly", "Assembling the Yat-sen Lion quadruped", "(max-width:900px) 100vw, 34vw")}
        <figcaption>Assembly &mdash; Yat-sen Lion, RAPID Lab</figcaption>
      </figure>
    </div>
  </div>
</section>

<section class="section" id="contact">
  <div class="wrap">
    <div class="section__head reveal">
      <h2 class="section__title">Get in touch</h2>
      <p class="eyebrow eyebrow--sig">{ME['programme']}</p>
    </div>
    <div class="reveal">
      <a class="contact__mail" href="mailto:{ME['email']}">{ME['email']}</a>
      <dl class="contact__grid">
        <div><dt>Based</dt><dd>{ME['location']}</dd></div>
        <div><dt>Code</dt><dd><a href="{ME['github']}" rel="noopener">github.com/liwanyue123</a></dd></div>
        <div><dt>Curriculum vitae</dt><dd>
          <a href="/assets/cv/wanyue-li-cv-en.pdf">English &darr;</a> &nbsp;
          <a href="/assets/cv/wanyue-li-cv-cn.pdf">中文 &darr;</a>
        </dd></div>
        <div><dt>Elsewhere</dt><dd><a href="/beyond/">Beyond the lab &nearr;</a></dd></div>
      </dl>
    </div>
  </div>
</section>

</main>
""" + footer()
    write("index.html", doc)

# ------------------------------------------------------------ project pages --
def build_projects():
    for i, p in enumerate(ALL):
        prev_p = ALL[i - 1] if i > 0 else None
        next_p = ALL[i + 1] if i < len(ALL) - 1 else None

        meta = [("Year", p["year"]), ("Role", p["role"]), ("Context", p["team"]),
                ("Focus", ", ".join(p["tags"]))]
        if p.get("links"):
            meta.append(("Links", "<br>".join(
                f'<a href="{u}" rel="noopener">{html.escape(t)} &nearr;</a>' for t, u in p["links"])))
        meta_html = "".join(
            f'<div class="p-meta__item"><dt>{html.escape(k)}</dt><dd>{v}</dd></div>' for k, v in meta)

        prose = []
        for h2, paras in p["body"]:
            prose.append(f"<h2>{html.escape(h2)}</h2>")
            prose += [f"<p>{t}</p>" for t in paras]

        if p.get("pub"):
            b = p["pub"]
            cls = ("chip--accepted"
                   if b["state"] in ("Accepted", "Published", "Best Paper Award")
                   else "chip--review")
            prose.append(f"""<h2>Publication</h2>
<article class="pub" style="border-top:1px solid var(--line)">
  <span class="pub__idx">[1]</span>
  <div>
    <h3 class="pub__title">{html.escape(b['title'])}</h3>
    <p class="pub__authors">{b['authors']}</p>
    <p class="pub__venue"><span class="chip">{html.escape(b['venue'])}</span>
    <span class="chip {cls}">{html.escape(b['state'])}</span></p>
  </div>
</article>""")

        if p.get("media"):
            prose.append("<h2>Gallery</h2>")
            prose += [media_block(m, p["dir"]) for m in p["media"]]

        nxt = []
        if prev_p:
            nxt.append(f'<a href="/work/{prev_p["slug"]}/"><div class="wrap" style="padding-inline:0">'
                       f'<p class="p-next__label">&larr; Previous</p>'
                       f'<p class="p-next__title">{html.escape(prev_p["title"])}</p></div></a>')
        if next_p:
            nxt.append(f'<a class="is-end" href="/work/{next_p["slug"]}/"><div class="wrap" style="padding-inline:0">'
                       f'<p class="p-next__label">Next &rarr;</p>'
                       f'<p class="p-next__title">{html.escape(next_p["title"])}</p></div></a>')

        if p.get("hero"):
            hero_html = f"""<header class="p-hero">
  <div class="p-hero__bg" aria-hidden="true">
    {picture(resolve(p['hero'], p['dir']), '', '100vw', loading='eager', pos=p['hero_pos'])}
  </div>
  <div class="p-hero__inner wrap">
    <a class="back-link" href="/#work">&larr; All work</a>
    <p class="eyebrow" style="margin-top:1.25rem">{p['year']} &middot; {html.escape(p['cat'])}</p>
    <h1 class="p-hero__title">{html.escape(p['title'])}</h1>
    <p class="lead">{p['lead']}</p>
  </div>
</header>"""
        else:
            hero_html = f"""<header class="p-hero p-hero--paper">
  <div class="p-hero__inner wrap">
    <a class="back-link" href="/#work">&larr; All work</a>
    <p class="eyebrow eyebrow--sig" style="margin-top:1.25rem">{html.escape(p.get('tile', p['year']))} &middot; {html.escape(p['cat'])}</p>
    <h1 class="p-hero__title">{html.escape(p['title'])}</h1>
    <p class="lead">{p['lead']}</p>
  </div>
</header>"""

        doc = head(f"{p['title']} — {ME['name']}", p["blurb"]) + nav() + f"""
<main>
{hero_html}

<div class="wrap">
  <div class="p-body">
    <dl class="p-meta">{meta_html}</dl>
    <div class="prose">{"".join(prose)}</div>
  </div>
</div>

<nav class="p-next wrap">{"".join(nxt)}</nav>
</main>
""" + footer()
        write(f"work/{p['slug']}/index.html", doc)

# ------------------------------------------------------------------ beyond --
def build_beyond():
    figs = "".join(
        f'<figure>{picture(s, c, "(max-width:700px) 100vw, 32vw")}</figure>'
        for s, c in GALLERY)
    doc = head(f"Beyond the lab — {ME['name']}",
               "Painting, 3D modelling and machine building — what Wanyue Li makes outside robotics."
               ) + nav("beyond") + f"""
<main>
<section class="section" style="border-top:0;padding-top:clamp(8rem,14vw,12rem)">
  <div class="wrap">
    <a class="back-link" href="/">&larr; Home</a>
    <h1 class="section__title reveal" style="font-size:clamp(2.5rem,7vw,5.5rem);margin-block:1.25rem 1.5rem">
      Beyond the lab
    </h1>
    <p class="lead reveal">
      I have a broad range of interests — painting, building 3D models, and making machinery.
      <span class="serif-em">Since becoming a graduate student there has not been much free time for any of it.</span>
    </p>
    <div class="gallery reveal" style="margin-top:clamp(3rem,6vw,5rem)">{figs}</div>
  </div>
</section>
</main>
""" + footer()
    write("beyond/index.html", doc)

# ------------------------------------------------------------------- assets --
FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="14" fill="#0A0A0B"/>
<path d="M12 20 L20 44 L28 28 L36 44 L44 20" fill="none" stroke="#EEEBE5"
      stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="52" cy="18" r="6" fill="#FF5D2E"/>
</svg>"""

ROBOTS = """User-agent: *
Allow: /

Sitemap: https://liwanyue123.github.io/sitemap.xml
"""

def build_extras():
    write("favicon.svg", FAVICON)
    write("robots.txt", ROBOTS)
    write(".nojekyll", "")
    urls = ["/", "/beyond/"] + [f"/work/{p['slug']}/" for p in ALL]
    body = "".join(
        f"<url><loc>https://liwanyue123.github.io{u}</loc>"
        f"<changefreq>monthly</changefreq></url>" for u in urls)
    write("sitemap.xml",
          '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + body + "</urlset>")
    # 404
    doc = head("Not found — " + ME["name"], "Page not found.") + nav() + f"""
<main class="wrap" style="min-height:80svh;display:flex;flex-direction:column;justify-content:center;gap:1.5rem">
  <p class="eyebrow eyebrow--sig">Error 404</p>
  <h1 class="section__title" style="font-size:clamp(2.5rem,8vw,6rem)">This page does not exist.</h1>
  <p class="lead">The link may be from the old site. Everything now lives under
     <a href="/#work" style="color:var(--sig)">Work</a>.</p>
  <p><a class="back-link" href="/">&larr; Back home</a></p>
</main>
""" + footer()
    write("404.html", doc)

# -------------------------------------------------------------------- write --
def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path) or ROOT, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  {rel:<40} {len(content.encode()) // 1024 or 1}KB")

def prune_orphans():
    """Delete work/<slug>/ directories left behind by renamed or removed projects."""
    live = {p["slug"] for p in ALL}
    wd = os.path.join(ROOT, "work")
    if not os.path.isdir(wd):
        return
    for name in sorted(os.listdir(wd)):
        if name not in live and os.path.isdir(os.path.join(wd, name)):
            shutil.rmtree(os.path.join(wd, name))
            print(f"  pruned orphan work/{name}/")


if __name__ == "__main__":
    print("building:")
    build_index()
    build_projects()
    build_beyond()
    build_extras()
    prune_orphans()
    print("done.")
