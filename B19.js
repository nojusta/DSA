class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    add(data) {
        let newNode = new Node(data);
        if (this.root === null) {
            this.root = newNode;
        } else {
            this.insertNode(this.root, newNode);
        }
    }

    insertNode(node, newNode) {
        if (newNode.data < node.data) {
            if (node.left === null) {
                node.left = newNode;
            } else {
                this.insertNode(node.left, newNode);
            }
        } else {
            if (node.right === null) {
                node.right = newNode;
            } else {
                this.insertNode(node.right, newNode);
            }
        }
    }

    getRootNode() {
        return this.root;
    }

    find(data) {
        return this.findNode(this.root, data);
    }

    findNode(node, data) {
        if (node === null) {
            return null;
        } else if (data < node.data) {
            return this.findNode(node.left, data);
        } else if (data > node.data) {
            return this.findNode(node.right, data);
        } else {
            return node;
        }
    }

    remove(data) {
        this.root = this.removeNode(this.root, data);
    }

    removeNode(node, key) {
        if (node === null) {
            return null;
        } else if (key < node.data) {
            node.left = this.removeNode(node.left, key);
            return node;
        } else if (key > node.data) {
            node.right = this.removeNode(node.right, key);
            return node;
        } else {
            if (node.left === null && node.right === null) {
                node = null;
                return node;
            }
            if (node.left === null) {
                node = node.right;
                return node;
            } else if (node.right === null) {
                node = node.left;
                return node;
            }

            let aux = this.findMinNode(node.right);
            node.data = aux.data;
            node.right = this.removeNode(node.right, aux.data);
            return node;
        }
    }

    findMinNode(node) {
        if (node.left === null) {
            return node;
        } else {
            return this.findMinNode(node.left);
        }
    }

    inorder(node) {
        if (node !== null) {
            node.left && this.inorder(node.left);
            console.log(node.data);
            node.right && this.inorder(node.right);
        }
    }

    preorder(node) {
        if (node !== null) {
            console.log(node.data);
            node.left && this.preorder(node.left);
            node.right && this.preorder(node.right);
        }
    }

    postorder(node) {
        if (node !== null) {
            node.left && this.postorder(node.left);
            node.right && this.postorder(node.right);
            console.log(node.data);
        }
    }
}
 
let bst = new BinarySearchTree();
bst.add(9);
bst.add(4);
bst.add(17);
bst.add(3);
bst.add(6);
bst.add(22);
bst.add(5);
bst.add(7);
bst.add(20);

let root = bst.getRootNode();
//bst.remove(9);
bst.find();
//bst.inorder(root);
//bst.preorder(root);
//bst.postorder(root);

/* 
        9
       / \
      4   17
     / \    \
    3   6    22
       / \   /
      5   7 20
*/