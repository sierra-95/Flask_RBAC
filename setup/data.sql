INSERT INTO roles (name) VALUES ('Admin'), ('Editor'), ('Viewer');

INSERT INTO permissions (name, description) VALUES
('manage_users', 'Can manage user accounts'),
('create_content', 'Can create content'),
('edit_content', 'Can edit content'),
('view_content', 'Can view content');

INSERT INTO role_permissions (role_id, permission_id) VALUES
((SELECT id FROM roles WHERE name = 'Admin'), (SELECT id FROM permissions WHERE name = 'manage_users')),
((SELECT id FROM roles WHERE name = 'Admin'), (SELECT id FROM permissions WHERE name = 'create_content')),
((SELECT id FROM roles WHERE name = 'Admin'), (SELECT id FROM permissions WHERE name = 'edit_content')),
((SELECT id FROM roles WHERE name = 'Admin'), (SELECT id FROM permissions WHERE name = 'view_content')),
((SELECT id FROM roles WHERE name = 'Editor'), (SELECT id FROM permissions WHERE name = 'create_content')),
((SELECT id FROM roles WHERE name = 'Editor'), (SELECT id FROM permissions WHERE name = 'edit_content')),
((SELECT id FROM roles WHERE name = 'Viewer'), (SELECT id FROM permissions WHERE name = 'view_content'));

INSERT INTO user_roles (user_id, role_id) VALUES
((SELECT id FROM users WHERE username = 'main'), (SELECT id FROM roles WHERE name = 'Admin')),
((SELECT id FROM users WHERE username = 'editor'), (SELECT id FROM roles WHERE name = 'Editor')),
((SELECT id FROM users WHERE username = 'viewer'), (SELECT id FROM roles WHERE name = 'Viewer'));
