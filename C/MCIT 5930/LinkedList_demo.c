#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Structure for a real estate property
typedef struct {
    int listing_num;
    char address[100];
    int bedrooms;
    int cost;
} real_estate;

// Structure for a node in the linked list
typedef struct Node {
    real_estate property;
    struct Node* next;
} Node;

// Function to create a new node
Node* createNode(real_estate property) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        perror("Error creating node");
        exit(EXIT_FAILURE);
    }

    newNode->property = property;
    newNode->next = NULL;

    return newNode;
}

// Function to insert a property into the linked list
Node* insertProperty(Node* head, real_estate property) {
    Node* newNode = createNode(property);

    // If the list is empty, make the new node the head
    if (head == NULL) {
        head = newNode;
    } else {
        // Otherwise, add the new node to the beginning of the list
        newNode->next = head;
        head = newNode;
    }

    return head;
}

// Function to print the properties on the same street
void printPropertiesOnStreet(Node* head, const char* street) {
    Node* current = head;

    printf("Properties on %s:\n", street);

    while (current != NULL) {
        if (strcmp(current->property.address, street) == 0) {
            printf("Listing Number: %d\n", current->property.listing_num);
            printf("Address: %s\n", current->property.address);
            printf("Bedrooms: %d\n", current->property.bedrooms);
            printf("Cost: %d\n", current->property.cost);
            printf("\n");
        }

        current = current->next;
    }
}

// Function to free the memory allocated for the linked list
void freeList(Node* head) {
    Node* current = head;
    Node* next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
}

int main() {
    Node* head = NULL;

    // Sample real estate properties
    real_estate property1 = {1, "123 Main St", 3, 200000};
    real_estate property2 = {2, "456 Oak St", 4, 300000};
    real_estate property3 = {3, "123 Main St", 2, 150000};

    // Insert properties into the linked list
    head = insertProperty(head, property1);
    head = insertProperty(head, property2);
    head = insertProperty(head, property3);

    // Print properties on the same street
    printPropertiesOnStreet(head, "123 Main St");

    // Free the memory allocated for the linked list
    freeList(head);

    return 0;
}
