# 💻 Virtual Memory & Page Replacement Simulator

## 📌 Project Overview
Virtual Memory & Page Replacement Simulator is an interactive web-based application developed using Python and Streamlit. It helps students understand how operating systems manage memory and replace pages when memory frames are full.

## 🎯 Objectives
- Understand the concept of Virtual Memory.
- Visualize page replacement techniques.
- Calculate Page Hits and Page Faults.
- Compare different page replacement algorithms.
- Understand memory management through an interactive interface.

## 🚀 Features
- Interactive user-friendly dashboard.
- Custom Page Reference String input.
- Adjustable number of memory frames.
- FIFO (First In First Out) Algorithm.
- LRU (Least Recently Used) Algorithm.
- Optimal Page Replacement Algorithm.
- Page Hit and Page Fault calculation.
- Performance graphs.
- Comparison of all three algorithms.

## 🛠️ Technologies Used
- Python
- Streamlit
- Pandas
- Matplotlib

## 📂 Project Structure

```text
Virtual-Memory-Simulator/
│
├── app.py
├── algorithms.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/palak304/Virtual-Memory-Simulator.git
```

2. Open the project folder:

```bash
cd Virtual-Memory-Simulator
```

3. Install the required libraries:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

## 🧠 Algorithms Explained

**1. FIFO (First In First Out)**

Replaces the page that entered memory first.

**2. LRU (Least Recently Used)**

Replaces the page that has not been used for the longest time.

**3. Optimal Page Replacement**

Replaces the page that will not be used for the longest time in the future.

## 📊 Expected Output
The application displays:
- Total Pages
- Page Hits
- Page Faults
- Hit Ratio
- Memory Frame Visualization
- Algorithm Performance Comparison

## 🎓 Project Information

**Project Title:** Virtual Memory & Page Replacement Simulator

**Domain:** Operating Systems

**Developed Using:** Python and Streamlit

## 👩‍💻 Author
Palak

---

*This project is developed for educational purposes to demonstrate Virtual Memory and Page Replacement concepts in Operating Systems.*