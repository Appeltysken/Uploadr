function uploadImage() {
  const form = document.getElementById('uploadForm');
  const gallery = document.querySelector('.gallery');
  const pending = document.createElement('div');
  pending.className = 'gallery-item pending';
  gallery.insertBefore(pending, gallery.children[1]);
  form.submit();
}