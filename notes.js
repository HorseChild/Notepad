let notes = []

function loadNotes() {
    const savedNotes = localStorage.getItem('quickNotes')
    return savedNotes ? JSON.parse(savedNotes) : []
}

function saveNote(event){ 
    event.preventDefault()

    const title = document.getElementById('noteTitle').value.trim()
    const content = document.getElementById('noteContent').value.trim()
    if (editingNoteId) {
        const noteIndex = notes.findIndex(note => note.id === editingNoteId)
        notes[noteIndex] = {
            ...notes[noteIndex],
            title:title,
            content:content
    }
    else{
    notes.unshift({
        id: generateId(),
        title:title,
        content:content
    })
    }

    saveNotes()
    renderNotes
}

function generateId() {
    return Date.now().toString()
}

function saveNotes() {
    localStorage.setItem('notes', JSON.stringify(notes))
}

function deleteNotes(noteId) {
    notes = notes.filter(note => note.id != noteId)
    saveNotes()
    renderNotes()
}

function renderNotes() {
    const notesContainer = document.getElementById('notesContainer');
    if (notesLength === 0) {
        notesContainer.innerHTML = `
        <div class="no-notes">
            <h2>No notes yet.</h2>
            <p> Create your first note! </p>
            <button class="add-note-btn" onclick="openNoteDialog()">+ Add Note</button>
        </div>
        `
        return
    }

    notesContainer.innerHTML = notes.map(note => `
        <div class="note-card">
            <h3 class="note-title">${note.title}</h3>
            <p class="note-content">${note.content}</p>
            <div class="note-actions">
                <button class="edit-btn" onclick="editNote('${note.id}')">Edit</button>
                <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#191b23">
                <path d="M184-184v-83.77l497.23-498.77q5.15-5.48 11.07-7.47 5.93-1.99 11.99-1.99 6.06 0 11.62 1.54 5.55 1.54 11.94 7.15l38.69 37.93q5.61 6.38 7.54 12 1.92 5.63 1.92 12.25 0 6.13-2.24 12.06-2.24 5.92-7.22 11.07L267.77-184H184Zm505.15-466.46L744-704.54 704.54-744l-54.08 54.85 38.69 38.69Z"/>
                </svg>
                <button class="delete-btn" onclick="deleteNote('${note.id}')">Delete</button>
                <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#191b23">
                <path d="M291-267.69 267.69-291l189-189-189-189L291-692.31l189 189 189-189L692.31-669l-189 189 189 189L669-267.69l-189-189-189 189Z"/>
                </svg>
            </div>
        </div>
    `).join('')
}

function openNoteDialog(noteId = null) {
    const dialog = document.getElementById('noteDialog')
    const titleInput = document.getElementById('noteTitle')
    const contentInput = document.getElementById('noteContent')

    if(note.id) {
        const noteToEdit = notes.find(n => n.id === noteId)
        editingNoteId = noteId
        document.getElementById('DialogTitle').textContent = 'Edit Note'
        titleInput.value = noteToEdit.title
        contentInput = noteToEdit.content
    }
    else {
        editingNoteId = null
        document.getElementById('DialogTitle').textContent = 'New Note'

    }

    dialog.showModal()
    titleInput.focus()

}

function closeNoteDialog() {
    document.getElementById('noteDialog').close()
}

function toggleTheme() {
    document.body.classList.toggle('dark-theme')
}

document.addEventListener('DOMContentLoaded', () => {
    renderNotes()
    document.getElementById('noteDialog').addEventListener('submit', saveNotes)
    document.getElementById('themeToggleBtn').addEventListener('click', toggleTheme)
    document.getElementById('noteDialog').addEventListener('click', function(event) {
        if (event.target === this) {
            closeNoteDialog()   
        }
    })
})
