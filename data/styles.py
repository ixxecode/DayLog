# | [ Dia 6 ]
# | ~/data/styles.py
# | Archivo que contiene el tema principal de mi app

# Tema principal [Oscuro]
DARK_THEME = """
QWidget {
    background-color: #121212;
    color: #d4d4d4;
    font-size: 14px;
}

/* Botones */
QPushButton {
    background-color: #2a2a2a;
    border: none;
    border-radius: 6px;
    padding: 6px 10px;
}

QPushButton:hover {
    background-color: #3a3a3a;
}

QPushButton:pressed {
    background-color: #444444;
}

/* Checkboxes */
QCheckBox {
    spacing: 6px;
}

QCheckBox::indicator {
    width: 16px;
    height: 16px;
}

QCheckBox::indicator:unchecked {
    border: 2px solid #555;
    border-radius: 4px;
    background: transparent;
}

QCheckBox::indicator:checked {
    background-color: #888;
    border: 2px solid #888;
    border-radius: 4px;
}

/* Labels */
QLabel {
    font-size: 14px;
}


/* ===== TITLE PANEL ===== */
#titleContainer {
    background-color: #1a1a1a;
    border-radius: 8px;
    padding: 8px;
    border: none;
}

#titleLabel {
    font-weight: bold;
    color: #e0e0e0;
}


/* ===== DAYS PANEL ===== */
#daysContainer {
    background-color: #181818;
    border-radius: 8px;
    padding: 10px;
    border: none;
}

/* Día actual */
#dayActive {
    color: #ffffff;
    font-weight: bold;
}

/* Días secundarios */
#dayMuted {
    color: #777777;
}
"""