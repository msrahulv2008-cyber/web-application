const API = 'http://127.0.0.1:8000/api/employees/';
let employees = [];

async function loadEmployees() {
  try {
    const response = await fetch(API);
    if (!response.ok) throw new Error('Backend not running');
    employees = await response.json();
    render();
  } catch (error) {
    document.getElementById('employees').innerHTML = '<tr><td colspan="8">Start the Django server to load employee records.</td></tr>';
  }
}

function render() {
  const search = document.getElementById('search').value.toLowerCase();
  const dept = document.getElementById('department').value;
  const status = document.getElementById('status').value;
  const list = employees.filter(e =>
    (!search || e.full_name.toLowerCase().includes(search) || e.employee_code.toLowerCase().includes(search)) &&
    (!dept || e.department === dept) && (!status || e.status === status)
  );
  document.getElementById('total').textContent = employees.length;
  document.getElementById('active').textContent = employees.filter(e => e.status === 'Active').length;
  document.getElementById('leave').textContent = employees.filter(e => e.status === 'On Leave').length;
  document.getElementById('resigned').textContent = employees.filter(e => e.status === 'Resigned').length;
  document.getElementById('employees').innerHTML = list.length ? list.map(e => `
    <tr><td>${e.employee_code}</td><td>${e.full_name}</td><td>${e.email}</td><td>${e.department}</td>
    <td>${e.designation}</td><td>₹${Number(e.salary).toLocaleString('en-IN')}</td><td>${e.status}</td>
    <td><button onclick='editEmployee(${e.id})'>Edit</button> <button class="danger" onclick='deleteEmployee(${e.id})'>Delete</button></td></tr>`).join('')
    : '<tr><td colspan="8">No employees found.</td></tr>';
}

function openModal() {
  document.getElementById('modal').style.display = 'flex';
  document.getElementById('modalTitle').textContent = 'Add Employee';
  document.querySelector('form').reset();
  document.getElementById('editId').value = '';
}
function closeModal() { document.getElementById('modal').style.display = 'none'; }

function editEmployee(id) {
  const e = employees.find(x => x.id === id);
  if (!e) return;
  openModal();
  document.getElementById('modalTitle').textContent = 'Edit Employee';
  document.getElementById('editId').value = e.id;
  document.getElementById('code').value = e.employee_code;
  document.getElementById('name').value = e.full_name;
  document.getElementById('email').value = e.email;
  document.getElementById('phone').value = e.phone;
  document.getElementById('dept').value = e.department;
  document.getElementById('designation').value = e.designation;
  document.getElementById('joining').value = e.date_of_joining;
  document.getElementById('salary').value = e.salary;
  document.getElementById('empStatus').value = e.status;
}

async function saveEmployee(event) {
  event.preventDefault();
  const id = document.getElementById('editId').value;
  const data = {
    employee_code: document.getElementById('code').value.trim(), full_name: document.getElementById('name').value.trim(),
    email: document.getElementById('email').value.trim(), phone: document.getElementById('phone').value.trim(),
    department: document.getElementById('dept').value, designation: document.getElementById('designation').value.trim(),
    date_of_joining: document.getElementById('joining').value, salary: Number(document.getElementById('salary').value),
    status: document.getElementById('empStatus').value
  };
  const response = await fetch(id ? API + id + '/' : API, { method: id ? 'PUT' : 'POST', headers: {'Content-Type':'application/json'}, body: JSON.stringify(data) });
  if (!response.ok) { alert('Please check the entered details.'); return; }
  closeModal(); await loadEmployees();
}

async function deleteEmployee(id) {
  if (!confirm('Delete this employee?')) return;
  const response = await fetch(API + id + '/', {method:'DELETE'});
  if (response.ok) loadEmployees(); else alert('Delete failed.');
}
function resetFilters() { document.getElementById('search').value=''; document.getElementById('department').value=''; document.getElementById('status').value=''; render(); }

window.onclick = e => { if (e.target === document.getElementById('modal')) closeModal(); };
loadEmployees();
