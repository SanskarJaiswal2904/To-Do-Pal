<template>
  <Navbar />
  <div class="page-container">
    <div class="content-wrap">
      <div class="container my-3">
        <div class="mb-3">
          <h2>Add Notes to Save:</h2>
          <br>
          <h3>Example text area:</h3>
          <br>
          <label for="textField" class="form-label">Title</label>
          <br>
          <textarea
            class="input-field"
            rows="1"
            placeholder="Title"
            v-model="title"
            required
          ></textarea>
          <br>
          <label for="textField" class="form-label">Description</label>
          <br>
          <textarea
            class="input-field"
            rows="10"
            placeholder="What you want to do today!"
            v-model="text"
            required
          ></textarea>
        </div>

        <button class="btn save-btn primary-btn" title="To save text" @click="saveText">
          Save <i class="fas fa-save"></i>
        </button>
        <button class="btn copy-btn primary-btn" title="To copy text to clipboard" @click="copyText">
          Copy to clipboard <i class="fas fa-copy"></i>
        </button>
      </div>
    </div>
    <div class="GettingUser">
      <SingleNote v-if="notes.length > 0" :items="notes" />
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import Footer from './Footer.vue';
import SingleNote from './SingleNote.vue';
import Navbar from './Navbar.vue';

const text = ref('');
const title = ref('');
const notes = ref([]);

const router = useRouter();

const saveText = async () => {
  try {
    const response = await axios.post('http://localhost:1024/notes', {
      title: title.value,
      description: text.value
    });

    if (response.status === 201) {
      const saveBtn = document.querySelector('.save-btn');
      if (saveBtn) {
        saveBtn.classList.add('clicked');

        setTimeout(() => {
          saveBtn.classList.remove('clicked');
          text.value = '';
          title.value = '';
        }, 750);

        const temp = {
          id: generateUniqueId(),
          title: title.value,
          description: text.value,
          datecreated: new Date().toLocaleString('en-GB')
        };

        notes.value.push(temp);
      }
    }
  } catch (error) {
    console.error('Error saving note:', error);
  }
};

function generateUniqueId() {
  return '_' + Math.random().toString(36).substr(2, 9);
}

onMounted(() => {
  let data = localStorage.getItem('user-info');
  if (!data) {
    router
      .push({ name: 'SignIn' })
      .then(() => {
        setTimeout(() => {
          location.reload();
        }, 0);
      });
  }
});

const copyText = () => {
  navigator.clipboard.writeText(title.value + " - " + text.value).then(
    () => {
      console.log('Text copied to clipboard');
    },
    (error) => {
      console.error('Error copying text:', error);
    }
  );

  const copyBtn = document.querySelector('.copy-btn');
  if (copyBtn) {
    copyBtn.classList.add('clicked');

    setTimeout(() => {
      copyBtn.classList.remove('clicked');
    }, 750);
  }
};
</script>


<style scoped>
body {
  margin: 0;
  padding: 0;
}

* {
  margin: 0;
  padding: 0;
}

.page-container {
  min-height: 100vh;
}

.page-container .content-wrap {
  margin-left: 60px;
  margin-top: 30px;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.mb-3 {
  margin-bottom: 1rem;
}

.form-label {
  margin-bottom: 1rem;
}

.input-field {
  width: 90%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
  resize: vertical;
}

.btn {
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  cursor: pointer;
  margin-right: 20px;
}

.primary-btn {
  background-color: white;
  color: blue;
  border-radius: 0.25rem;
  padding: 0.5rem 1rem;
  border: 1px solid #007bff;
}

.primary-btn:hover {
  background-color: blue;
  color: white;
}

.delete-btn {
  border: 1px solid red;
  background-color: white;
  color: red;
}

.delete-btn:hover {
  background-color: red;
  color: white;
}

.clicked {
  background-color: rgb(15, 195, 15);
  color: white;
}
</style>




